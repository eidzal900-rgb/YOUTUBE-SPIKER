import streamlit as st
import json
import os

st.title("YouTube Viral Dashboard")

path = os.path.join("data","niche_rank.json")

if os.path.exists(path):
    with open(path) as f:
        data = json.load(f)
else:
    data = {}

for niche in data:

    st.header(niche)

    for v in data[niche]:

        st.write(v["title"])
