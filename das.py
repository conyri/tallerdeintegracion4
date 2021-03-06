import streamlit as st 
import pandas as pd 
import numpy as np 
import pydeck as pdk 
import altair as alt 
from datetime import datetime

from pymongo import MongoClient
import pymongo
import time as ti


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def get_client():
    return MongoClient("mongodb+srv://constanza:constanza@cluster0.getl7.mongodb.net/integracion4?retryWrites=true&w=majority")

client = get_client()
db = client.integracion4
st.sidebar.subheader ("MongoDB:")
coll_name = st.sidebar.selectbox ("Select collection: ",db.list_collection_names())
@st.cache
def load_mongo_data(coll_name):
    data = db.coll_name.find()
    for documents in data:
        print(documents)

st.write("Showing data for: ", coll_name)
st.write(load_mongo_data(coll_name))
st.write(db.coll_name.find())

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')