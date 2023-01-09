import streamlit as st
import requests
from json import loads
import re
import base64

@st.cache
def requete(catégories, recherche):
    attributes = f"{catégories}/"
    research = f'?search={recherche}'
    response = requests.get(f"https://swapi.dev/api/{attributes}{research}")
    bytes_json = response.content
    final_json = loads(bytes_json)
    if final_json["next"]:
        r = final_json['results']
        while final_json["next"]:
            response = requests.get(final_json["next"])
            bytes_json = response.content
            final_json = loads(bytes_json)
            r.extend(final_json["results"])
            try:
                page_match = re.search(r'page=(\d+)', final_json["next"])
                page = int(page_match.group(1))
                next_page_url = f'https://swapi.dev/api/{catégories}/?search={recherche}&page={page}'
                final_json["next"] = next_page_url
            except:
                final_json["next"] = None
        return r
    return final_json["results"]


def afficher_information(recherche, ma_requete, choices):
    if recherche == "":
        st.write(f"We found {len(ma_requete)} results for your search, {choices} found are :")
        st.write(', '.join([ma_requete[i][list(ma_requete[i].keys())[0]] for i in range(len(ma_requete))]))
    else:
        if len(ma_requete) == 0:
            st.write("We have no answer to your request !")
        elif len(ma_requete) == 1:
            st.write(f"We found {len(ma_requete)} results for your search, {choices} found are :")
            st.write(ma_requete[0][list(ma_requete[0].keys())[0]])
        else:
            st.write(f"We found {len(ma_requete)} results for your search '{recherche}', {choices} found are :")
            st.write(', '.join([ma_requete[i][list(ma_requete[i].keys())[0]] for i in range(len(ma_requete))]))


def draw_background_image():
  st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://lumiere-a.akamaihd.net/v1/images/star-wars-backgrounds-25_bc15ec98.jpeg");
        background-size: cover;
        background-repeat: repeat;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True)


def decode_binary_image(image_binary_path):
    with open(image_binary_path, 'rb') as image_file:
        image_content = image_file.read()
        image = base64.b64decode(image_content)
        return image
