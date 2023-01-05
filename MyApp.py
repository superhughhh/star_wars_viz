import streamlit as st
import pandas as pd
import requests
from json import loads
import re


api_key = ['films', 'people', 'planets', 'species', 'starships', 'vehicles']
choices = st.selectbox("Catégories", api_key)
research_input = st.text_input("research")


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

ma_requete = requete(choices, research_input)


def afficher_information(recherche, ma_requete):
    if recherche == "":
        st.write(f"Nous avons trouvé {len(ma_requete)} résultats à votre recherche '{recherche}', les {choices} trouvé(es) sont :")
        st.write(', '.join([ma_requete[i][list(ma_requete[i].keys())[0]] for i in range(len(ma_requete))]))
    else:
        if len(ma_requete) == 0:
            st.write("Nous n'avons pas de réponse à votre requête")
        elif len(ma_requete) == 1:
            st.write(f"Nous avons trouvé {len(ma_requete)} résultats à votre demande, le {choices} trouvé(e) est :")
            st.write(ma_requete[0][list(ma_requete[0].keys())[0]])
        else:
            st.write(f"Nous avons trouvé {len(ma_requete)} résultats à votre recherche '{recherche}', les {choices} trouvé(es) sont :")
            st.write(', '.join([ma_requete[i][list(ma_requete[i].keys())[0]] for i in range(len(ma_requete))]))



afficher_information(research_input, ma_requete)
