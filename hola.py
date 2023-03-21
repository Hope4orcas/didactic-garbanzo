import streamlit as st
import requests

st.title("ISS INFO")

posicion_iss = requests.get("http://api.open-notify.org/iss-now.json")
json_iss = posicion_iss.json()
st.json(json_iss)
st.table(json_iss)
st.write(json_iss["iss_position"]["latitude"])
st.write(json_iss["iss_position"]["longitude"])

latitud=json_iss["iss_position"]["latitude"]
longitud=json_iss["iss_position"]["longitude"]
posicion=f"https://maps.google.com/?q={latitud},{longitud}"
st.write(posicion)

st.title("ASTRONAUTS TODAY")
atronautas_iss=requests.get("http://api.open-notify.org/astros.json")
astronautas=atronautas_iss.json()
st.table(astronautas["people"])
