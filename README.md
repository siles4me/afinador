# Afinador de cuerdas para guitarra utilizando la transformada de Fourier

## Proyecto calculo empresarial, Lead University

### Autores: Guisselle Betancur y David Siles

## Descripción

La idea de este proyecto es crear una aplicación de afinador de cuerdas de guitarra utilizando la transformada de Fourier para analizar las frecuencias presentes en una grabación de audio de una cuerda de guitarra. La aplicación graba un fragmento de audio, calcula su espectro de frecuencia a través de la transformada de Fourier y determina qué cuerda de la guitarra está siendo tocada en función de la frecuencia fundamental detectada.

## Funcionamiento

Esta aplicacón se desarrolló para ser utilizada en streamlit, a través de un entorno de python, aplicando las técnicas aprendidas para su funcionalidad, donde se utilizaron las siguientes librerías

- `streamlit`
- `audio_recorder_streamlit`
- `numpy`
- `scipy`
- `plotly`
- `PIL` (Python Imaging Library)

#### 

## Transformada de Fourier

La ecuación utilizada en el proyecto para calcular la transformada de Fourier de la señal de audio, es la siguiente:

Transformada de Fourier discreta (DFT) de una señal $x[n]$ de longitud $N$ se calcula mediante la siguiente ecuación:

$$
X[k] = \sum_{n=0}^{N-1}x[n]* e^{-j2\pi*\frac{kn}{n}}
$$

Donde:

- $X[k]$ es el valor en la frecuencia $k$ de la DFT.
- $x[n]$ es el valor de la señal en el instante $n$.
- $N$ es la longitud de la señal.
- $j$ es la unidad imaginaria $(j^2 = -1)$.
- $k$ varía desde $0$ hasta $N-1$, representando las frecuencias discretas.

En el proyecto, esta ecuación se aplica a la señal de audio grabada para calcular su espectro de frecuencia, que luego se utiliza para determinar la afinación de la cuerda tocada.

Esto se representa  la transformada de Fourier en el código utilizando la biblioteca `scipy` de la siguiente manera:

```python
# Realizar la transformada de Fourier de la señal de audio
gk = fourier.fft(Audio_m)

# Calcular la magnitud del espectro de frecuencia
M_gk = abs(gk)
M_gk = M_gk[0:L // 2]

# Calcular la fase del espectro de frecuencia
Ph_gk = np.angle(gk)

# Calcular las frecuencias correspondientes al espectro
F = Fs * np.arange(0, L // 2) / L
```

Este este fragmento de código, demuestra como se utiliza la función `fourier.fft()` de la biblioteca `scipy.fftpack` para calcular la transformada de Fourier de la señal de audio `Audio_m`. Luego, se calcula la magnitud del espectro de frecuencia (`M_gk`) a partir de la parte real e imaginaria de la transformada de Fourier. La variable `F` representa las frecuencias correspondientes a las muestras del espectro.

Este cálculo se realiza para analizar las frecuencias presentes en la señal de audio y determinar la frecuencia fundamental de la cuerda tocada, lo cual se utiliza para identificar la afinación de la cuerda.

## Streamlit

Streamlit al ser  biblioteca de Python que permite crear aplicaciones web interactivas con solo unos pocos pasos. En este proyecto de afinador de cuerdas de guitarra, Streamlit se utiliza para construir la interfaz de usuario y mostrar los resultados de análisis de audio y afinación.

### En el código

Dentro de la función `main()` en el código, Streamlit se utiliza para crear diferentes componentes de la interfaz de usuario y mostrar los resultados:

1. **Título y Encabezado:**
   
   El título y los créditos del proyecto se agregan con las funciones `st.title()` y `st.write()`
   
   ```python
   st.title("Afinador de Cuerdas de Guitarra")
   st.write("Proyecto Cálculo, Guisselle Betancur y David Siles")
   ```

2. **Botón de Iniciar Grabación:**
   
   El botón para iniciar la grabación se crea con `st.button()`
   
   ```python
   if st.button("Iniciar Grabación"):
       # Lógica para la grabación de audio y análisis posterior
   ```

3. **Gráfico de Espectro de Frecuencia:**
   
   Se utiliza el componente `st.plotly_chart()` para mostrar el gráfico interactivo del espectro de frecuencia."
   
   ```python
   fig = px.line(x=F, y=M_gk, title="Espectro de Frecuencia", labels={'x': 'Frecuencia (Hz)', 'y': 'Amplitud FFT'})
   st.plotly_chart(fig, use_container_width=True)
   ```

4. **Mensajes de Afinación:**
   
   Los resultados de análisis se muestran utilizando las funciones de escritura de Streamlit, como `st.write()`
   
   ```python
   st.write(f"🟢 La cuerda grabada está afinada. Es la cuerda {closest_string}. Frecuencia detectada: {F_fund:.2f} Hz.")
   ```

# 

Documentación de la Aplicación de Afinador de Cuerdas de Guitarra

La Aplicación de Afinador de Cuerdas de Guitarra es una herramienta en línea que utiliza la transformada de Fourier para analizar las frecuencias presentes en una grabación de audio de una cuerda de guitarra. La aplicación determina la afinación de la cuerda tocada y proporciona retroalimentación sobre si la cuerda está afinada correctamente o necesita ser ajustada.

## Acceso a la Aplicación

La aplicación está disponible en línea en la siguiente dirección: [Afinador de Cuerdas de Guitarra](https://brhpvwrnr7yjgcmwtrfp2m.streamlit.app/). Puedes acceder a la aplicación utilizando un navegador web en cualquier dispositivo compatible.

## Uso de la Aplicación

1. Al acceder al enlace proporcionado, se cargará la página de la aplicación en tu navegador.

2. En la página principal de la aplicación, encontrarás el título "Afinador de Cuerdas de Guitarra" y los créditos del proyecto.

3. Para comenzar, haz clic en el botón "Iniciar Grabación". Esto activará la funcionalidad de grabación de audio.

4. Toca una cuerda de guitarra de manera que el audio de la cuerda se grabe durante unos segundos.

5. Después de detener la grabación, la aplicación procesará el audio grabado y calculará la frecuencia fundamental de la cuerda tocada.

6. La aplicación mostrará un gráfico que representa el espectro de frecuencia de la grabación, lo que te permite visualizar las frecuencias detectadas.

7. A continuación, la aplicación determinará qué cuerda de guitarra corresponde a la frecuencia fundamental detectada.

8. La aplicación te proporcionará un mensaje indicando si la cuerda está afinada correctamente o si necesita ser ajustada. El mensaje también te dirá si debes afinar hacia arriba o hacia abajo para lograr la afinación adecuada.

9. Además, se mostrará una imagen que contiene una tabla de afinación para que puedas comparar la frecuencia detectada con las frecuencias objetivo de cada cuerda de guitarra.

## Notas Adicionales

- Asegúrate darle acceso al micrófono al navegador para que la grabación de audio funcione correctamente.

- Ten en cuenta que la precisión de la detección de afinación puede variar según la calidad del audio y la precisión de la interpretación. Los resultados pueden ser más precisos si se utiliza un entorno de grabación controlado.

- Esta aplicación es útil para afinar las cuerdas de una guitarra estándar, con las afinaciones E2, A, D, G, B y E4. Si estás utilizando una afinación alternativa, los resultados pueden no ser precisos.

## Conclusión

La Aplicación de Afinador de Cuerdas de Guitarra es una herramienta práctica y fácil de usar para guitarristas que desean afinar sus cuerdas de manera precisa. La combinación de la transformada de Fourier y la retroalimentación visual hacen que la tarea de afinar una guitarra sea más intuitiva y efectiva.
