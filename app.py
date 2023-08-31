import streamlit as st
from audiorecorder import audiorecorder
import numpy as np
from scipy.io import wavfile
import scipy.fftpack as fourier
import plotly.express as px
from PIL import Image

def main():
    st.title("Afinador de Cuerdas de Guitarra")
    st.write("Grabar audio")
    # Agregamos la grabación del archivo de audio
    audio_bytes = audio_recorder()
    if audio_bytes:
        # Guardar el audio grabado en un archivo
        with open('grabacion.wav', 'wb') as f:
            f.write(audio_bytes)

        # Leer el archivo de audio grabado y obtener la frecuencia de muestreo y los datos
        Fs, Audio_m = wavfile.read('grabacion.wav')
        Audio_m = Audio_m[:, 0]  # Nos quedamos con un solo canal

        L = len(Audio_m)
        n = np.arange(0, L) / Fs
        gk = fourier.fft(Audio_m)
        M_gk = abs(gk)
        M_gk = M_gk[0:L // 2]
        Ph_gk = np.angle(gk)
        F = Fs * np.arange(0, L // 2) / L

        # Agregar visualización con Plotly Express
        fig = px.line(x=F, y=M_gk, title="Espectro de Frecuencia", labels={'x': 'Frecuencia (Hz)', 'y': 'Amplitud FFT'})
        st.plotly_chart(fig, use_container_width=True)

        # Identificación de la nota musical
        Posm = np.where(M_gk == np.max(M_gk))
        F_fund = F[Posm][0]

        target_frequencies = {
            'E2': 82.40,
            'A': 110.00,
            'D': 146.83,
            'G': 195.99,
            'B': 246.94,
            'E4': 329.63
        }

        closest_string = min(target_frequencies, key=lambda x: abs(target_frequencies[x] - F_fund))
        target_freq = target_frequencies[closest_string]

        if abs(F_fund - target_freq) < 5:
            st.write(f":green[La cuerda grabada está afinada. Es la cuerda {closest_string}. Frecuencia detectada: {F_fund:.2f} Hz.]")
        elif F_fund < target_freq:
            st.write(f":red[La cuerda grabada está desafinada. Debe ser la cuerda {closest_string}. Afinar hacia arriba. Frecuencia detectada: {F_fund:.2f} Hz.]")
        else:
            st.write(f":red[La cuerda grabada está desafinada. Debe ser la cuerda {closest_string}. Afinar hacia abajo. Frecuencia detectada: {F_fund:.2f} Hz.]")

        image = Image.open('Afinacion.jpeg')
        st.image(image, caption='Tabla Afinación')

if __name__ == "__main__":
    main()
