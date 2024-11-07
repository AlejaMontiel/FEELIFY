# Feelify: Your Mood, Your Music
Feelify es una app inteligente que utiliza reconocimiento facial y de voz para ofrecer recomendaciones de música personalizadas basadas en el estado de ánimo.

## Características
- Detección de emociones a través de Teachable Machine.
- Recomendación de playlists según el estado de ánimo detectado.
- Control de luces LED (simulado con Wokwi).
- Interfaz intuitiva en Streamlit para una experiencia de usuario fluida.

## Requisitos
- Python 3.x
- Streamlit
- TensorFlow.js (para el modelo exportado de Teachable Machine)

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/Feelify.git
   ```
2. Navega a la carpeta `streamlit_app/` e instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución
```bash
streamlit run streamlit_app/feelify_app.py

## Simulación de LEDs
Para simular los LEDs con Wokwi, [abre esta simulación](https://wokwi.com/simulations/tu-enlace).

