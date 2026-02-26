import streamlit as st
from PIL import Image
st.title("Mi primera app")
st.header("Esta es mi página de presentación")
image= Image.open ("imagen mariposa.jpg")
st.image(image,caption= "Esta es mi imagen")
