# The-Genre-Lab---Music-Genre-Classification

🎵 The Genre Lab – Music Genre Classification with Deep Learning

---

📚 Table of Contents

About the Project

Dataset

Preprocessing

Deep Learning Model

Web Application - Flask

Database

MP3 Support

Screenshots


How to Run

Results & Accuracy

Tools & Technologies

Contact



---

🎯 About the Project

The Genre Lab is an intelligent music genre classifier powered by deep learning, created to accurately identify music genres from audio signals. Built as a part of a capstone project by students at Avanthi Institute of Engineering and Technology during the SAP Code Unnati program, the system uses feature extraction and CNN-based modeling for accurate prediction and integrates seamlessly with a web interface for ease of use.


---

🎧 Dataset

We used the widely adopted GTZAN Dataset, which consists of:

1,000 audio tracks

10 genre classes: Blues, Classical, Country, Disco, HipHop, Jazz, Metal, Pop, Reggae, Rock

Each track is 30 seconds long in WAV format


> This dataset is excellent for evaluating audio classification models.




---

🛠️ Preprocessing

To process audio efficiently and prepare it for model training, we followed these steps:

Feature Extraction (Librosa):

Mel-Frequency Cepstral Coefficients (MFCCs)

Chroma Features

Spectral Contrast


Each 30-second clip was segmented into 10 chunks for better model generalization.

y, sample_rate = librosa.load(file_path, sr=22050)
mfcc = librosa.feature.mfcc(y, sample_rate, n_mfcc=13, n_fft=2048, hop_length=512)


---

🧠 Deep Learning Model

We experimented with various architectures (ANN, LSTM), but the best performance came from a Convolutional Neural Network (CNN).

Model Architecture:

3 Convolutional Layers

Batch Normalization & Dropout

Fully Connected Dense Layers

Softmax Activation


Accuracy: ~80% on test data.


---

🌐 Web Application - Flask

We built a clean Flask-based interface with:

Home – Upload an audio file to classify

Project – Overview of the technology

About – Team details

Contact – Email + DB integration


🗃️ Database

MySQL is used to store contact form responses:

CREATE TABLE contacts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fullname VARCHAR(30),
  email VARCHAR(30),
  phone_number VARCHAR(50),
  url VARCHAR(50),
  message TEXT,
  reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


---

🔊 MP3 Support

To support .mp3 files, we used FFMPEG + Pydub to:

Convert MP3 ➝ WAV

Trim relevant parts before prediction


> ✅ Ensure FFMPEG is in system


---


🧪 Results & Accuracy

Training Accuracy: 85%

Validation Accuracy: 80%



---

🚀 How to Run

# 1. Clone the repository
git clone 
https://github.com/Srinivas-Vid/The-Genre-Lab---Music-Genre-Classification.git

# 2. Navigate to the project directory
cd Music-Genre-Classification

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run the Flask application
python TheGenreLab.py


---

🧰 Tools & Technologies

Python (Librosa, TensorFlow, NumPy)

Flask – Web Framework

MySQL – Database

HTML/CSS/JS – Frontend

FFMPEG & Pydub – Audio Processing



---

📬 Contact

Developed by:

Srinivas Erramalla & Team

Avanthi Institute of Engineering and Technology

📍 Hyderabad, India

📧 srinivaserramalla5@gmail.com 


---
