document.getElementById("audio-upload").addEventListener("change", changeHandler);

function changeHandler({ target }) {
    if (!target.files.length) return;
    
    const urlObj = URL.createObjectURL(target.files[0]);
    const audio = document.createElement("audio");
    
    audio.addEventListener("load", () => {
        URL.revokeObjectURL(urlObj);
    });
    
    const newItem = document.createElement("li");
    newItem.appendChild(audio);
    const list = document.getElementById("myList");
    list.insertBefore(newItem, list.childNodes[0]);
    
    audio.controls = true;
    audio.src = urlObj;
    audio.classList.add("audio-preview"); // For styling
}