import streamlit as st
import api_request



api_key = ['films', 'people', 'planets', 'species', 'starships', 'vehicles']
choix = st.selectbox("Catégories", api_key)
research_input = st.text_input("research")


ma_requete = api_request.requete(choix, research_input)


api_request.afficher_information(research_input, ma_requete, choix)
