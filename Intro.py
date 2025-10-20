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
 st.write("En el siguiente enlace veremos como puedes transcribir y traducir contenido de imágenes incluso usando la cámara.") 
 url = "https://ocraudiotextdiego.streamlit.app/#reconocimiento-optico-de-caracteres"
 st.write(f"Imágenes ocr [Enlace]({url})")

with col2: 
 st.subheader("Análisis de PDF")
 image = Image.open('lilbro.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos análisis con IA de documentos de PDF con palabras clave y explicaciones tipo profesor.") 
 url = "https://chatpdfdiego.streamlit.app/"
 st.write(f"PDF: [Enlace]({url})")

 st.subheader("Control por voz Wokwi")
 image = Image.open('controldog.jpg')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos como controlar enviar mensajes que llegan a la interfaz de wokwi") 
 url = "https://ctrlvoicediego.streamlit.app/"
 st.write(f"Voz en Wokwi: [Enlace]({url})")

 st.subheader("Detección de números escritos a mano")
 image = Image.open('monopiensa.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos como detectar números escribiendo a mano.") 
 url = "https://handwrittingtest.streamlit.app/"
 st.write(f"Tablerito: [Enlace]({url})")


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


