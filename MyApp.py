import streamlit as st
import api_request
import time
import base64

with open('encoded_logo_image.txt', 'rb') as image_file:
    image_content = image_file.read()
    image_png = base64.b64decode(image_content)
st.image(image_png)


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
    ma_requete = api_request.requete(choix, research_input)
    stop = time.time()
    with col2:
        st.write(f'Search-time : {int(stop-start)} seconds')
    api_request.afficher_information(research_input, ma_requete, choix)
