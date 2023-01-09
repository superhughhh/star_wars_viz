import streamlit as st
from my_function import *
import time


draw_background_image()
st.image(decode_binary_image('binary_image/encoded_logo_image.txt'))


st.write("##")
st.write("##")


api_key = ['films', 'people', 'planets', 'species', 'starships', 'vehicles']

choix = st.radio("Class", api_key, horizontal=True)
research_input = st.text_input(label="Regex Researching")
col1, col2 = st.columns(2)
with col1:
    button = st.button("Search", type="primary")


st.write("##")
st.write("##")


if button:
    start = time.time()
    ma_requete = function.requete(choix, research_input)
    stop = time.time()
    with col2:
        st.write(f'Search-time : {int(stop-start)} seconds')
    afficher_information(research_input, ma_requete, choix)
