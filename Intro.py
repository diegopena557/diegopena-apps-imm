import streamlit as st
from PIL import Image
st.title("Portafolio de aplicaciones")

with st.sidebar:
  st.subheader("Portafolio de aplicaciones por Diego Peña")
  parrafo = (
    "Les presento mi portafolio de aplicaciones realizadas para interfaces multimodales."
    "Es muy interesante ver todo lo que se puede hacer y pensar aplicaciones diversas para todo."
    "Muchas gracias."
  )
  st.write(parrafo)

url_ia="https://diegopenapp.streamlit.app/"
st.subheader("En el siguiente enlace puedes encontrar la primera pagina e intro de streamlit")
st.write(f"Enlace para intro [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz")
 image = Image.open('unclebao.jpg')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se convierte el texto a voz") 
 url = "https://ttstestdiego.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Traductor de voz a texto Inglés y español")
 image = Image.open('huhbao.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos traducciones a varios idiomas con input de voz") 
 url = "https://traductortestdiego.streamlit.app/"
 st.write(f"Traductor [Enlace]({url})")

 st.subheader("Reconocimiento de texto en imágenes")
 image = Image.open('estudiado.png')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos commo puedes transcribir y traducir contenido de imágenes incluso usando la cámara.") 
 url = "https://ocraudiotextdiego.streamlit.app/#reconocimiento-optico-de-caracteres"
 st.write(f"Imágenes ocr [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductor-ab0sp9f6fi.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://asistpy-csv.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


