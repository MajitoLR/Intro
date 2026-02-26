import streamlit as st
from PIL import Image
st.title("Mi primera app")
st.header("Esta es mi página de presentación")
image= Image.open ("imagen mariposa.jpg")
st.image(image,caption= "Esta es mi imagen")
texto= st.text_input ("Ingresa texto","texto inicial")
st.write("El texto que escribiste es",texto)
if st.button("Presiona el botón"):
  st.write("Presonaste el botón")
