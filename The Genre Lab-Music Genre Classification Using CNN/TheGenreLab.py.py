from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import smtplib
from flask_mysqldb import MySQL
from datetime import datetime
import tensorflow as tf
import keras
import librosa
import numpy as np
import math
import subprocess
import os
from pydub import AudioSegment

app = Flask(__name__, static_folder='static')

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Srinivas@2824"
app.config['MYSQL_DB'] = "music_genre_db"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

model = keras.models.load_model("MusicGenre_CNN_79.73.h5")

@app.route("/")
def homepage():
    title = "MGC"
    return render_template('homepage.html', title=title)

@app.route("/prediction", methods=["POST"])
def prediction():
    title = "MGC | Prediction"
    audio = request.files['myfile']

    if audio.filename == '':
        return "No file selected", 400

    audio_filename = secure_filename(audio.filename)
    audio.save(audio_filename)

    if audio_filename.endswith(".mp3"):
        extension = os.path.splitext(audio_filename)[0]
        try:
            command = f'ffmpeg -i "{audio_filename}" "{extension}.wav" -y'
            subprocess.run(command, shell=True, check=True)
            audio_filename = extension + '.wav'
        except Exception as e:
            print(f"Error converting audio: {e}")
            return "Error converting audio file", 500

        t1 = 60 * 1000
        t2 = 90 * 1000
        newAudio = AudioSegment.from_wav(audio_filename)
        newAudio = newAudio[t1:t2]
        newAudio.export(audio_filename, format="wav")

    def process_input(audio_file, track_duration):
        SAMPLE_RATE = 22050
        NUM_MFCC = 13
        N_FTT = 2048
        HOP_LENGTH = 512
        SAMPLES_PER_TRACK = SAMPLE_RATE * track_duration
        samples_per_segment = int(SAMPLES_PER_TRACK / 10)
        signal, sample_rate = librosa.load(audio_file, sr=SAMPLE_RATE)
        mfcc = librosa.feature.mfcc(signal[:samples_per_segment], sample_rate, n_mfcc=NUM_MFCC, n_fft=N_FTT, hop_length=HOP_LENGTH)
        return mfcc.T

    audio_file = process_input(audio_filename, 30)
    genre_dict = {0: "disco", 1: "pop", 2: "classical", 3: "metal", 4: "rock", 5: "blues", 6: "hiphop", 7: "reggae", 8: "country", 9: "jazz"}
    X_to_predict = audio_file[np.newaxis, ..., np.newaxis]
    pred = model.predict(X_to_predict)
    pred = np.argmax(pred)
    prob = model.predict(X_to_predict)
    for result in prob:
        proba = str("{:.2f}".format((max(result) * 100)))

    L = np.argsort(result)

    return render_template('prediction.html', title=title, prediction=genre_dict[int(pred)], probability=proba,
                           second_prediction=genre_dict[L[-2]], second_probability=("{:.2f}".format((result[L[-2]] * 100))),
                           third_prediction=genre_dict[L[-3]], third_probability=("{:.2f}".format((result[L[-3]] * 100))))

@app.route("/about")
def about():
    title = "MGC | About"
    return render_template('about.html', title=title)

@app.route("/project")
def project():
    title = "MGC | Project"
    return render_template('project.html', title=title)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        url = request.form['url']
        message = request.form['message']
        time = datetime.now()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("srinivaserramalla5@gmail.com", "cnbs jbfz zvle vtog")
        server.sendmail("srinivaserramalla5@gmail.com", email, message)

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO Contacts VALUES(%s,%s,%s,%s,%s,%s,%s)''', (None, full_name, email, phone_number, url, message, time))
        mysql.connection.commit()
        cursor.close()

        title = "MGC | Contact"
        return render_template('contact.html', title=title)

@app.route("/contact")
def contact():
    title = "MGC | Contact"
    return render_template('contact.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)
