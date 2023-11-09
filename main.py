import streamlit as st

import cowsay

st.write("Ma super app !")

text = st.text_input(label="Que veux tu faire dire à l'animal ?")
cut_pet = st.selectbox(label="Quel animal doit parler ?", options=[pet for pet in cowsay.list_cows()])

if text and cut_pet:
    st.text(cowsay.cowthink(text, cut_pet))