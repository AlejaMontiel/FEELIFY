import streamlit as st
import cv2
import numpy as np
from tensorflow import keras

# Encabezado y bienvenida
st.title("Feelify: Your Mood, Your Music 🎶")
st.subheader("Analizando tu estado de ánimo para ofrecerte la música perfecta")


# Configuración de la cámara
def capture_image():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    camera.release()
    if ret:
        return frame
    else:
        return None

# Mostrar imagen en la app y capturar estado de ánimo
if st.button("Analizar mi estado de ánimo"):
    frame = capture_image()
    if frame is not None:
        st.image(frame, channels="BGR", caption="Imagen capturada")
        # Procesar la imagen (preprocesamiento) y analizarla con el modelo
    else:
        st.error("No se pudo capturar la imagen.")

from tensorflow.keras.models import load_model

# Cargar el modelo (coloca el archivo del modelo en teachable_machine/emotion_model.h5)
model = load_model("teachable_machine/emotion_model.h5")

def predict_emotion(frame):
    # Preprocesamiento de la imagen (tamaño, normalización)
    resized_frame = cv2.resize(frame, (224, 224))  # Tamaño que requiere el modelo
    normalized_frame = resized_frame / 255.0  # Normalizar píxeles
    # Predicción
    prediction = model.predict(np.expand_dims(normalized_frame, axis=0))
    emotion = np.argmax(prediction)  # Clase de emoción más probable
    return emotion

if frame is not None:
    emotion = predict_emotion(frame)
    st.write(f"Estado de ánimo detectado: {emotion}")

# Crear playlists de ejemplo para cada estado de ánimo
playlists = {
    "feliz": ["Canción 1", "Canción 2"],
    "triste": ["Canción 3", "Canción 4"],
    "enojado": ["Canción 5", "Canción 6"]
}

# Función para recomendar playlist
def recommend_playlist(emotion):
    if emotion == "feliz":
        return playlists["feliz"]
    elif emotion == "triste":
        return playlists["triste"]
    elif emotion == "enojado":
        return playlists["enojado"]
    else:
        return ["Canción genérica"]

# Mostrar playlist en la app
playlist = recommend_playlist(emotion)
st.write("Tu playlist personalizada:")
for song in playlist:
    st.write(song)






