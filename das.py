import streamlit as st 
import pandas as pd 
import numpy as np 
import pydeck as pdk 
import altair as alt 
from datetime import datetime

from pymongo import MongoClient
import pymongo
import time as ti

myclient = pymongo.MongoClient("mongodb+srv://constanza:constanza@cluster0.getl7.mongodb.net/integracion4?retryWrites=true&w=majority")

mydb = myclient["integracion4"]
mycol = mydb["regiones"]

mydoc = mycol.find()


 #select box
metrics =['Atacama','','total_deaths','new_deaths','total_cases_per_million','new_cases_per_million','total_deaths_per_million','new_deaths_per_million','total_tests','new_tests','total_tests_per_thousand','new_tests_per_thousand']
cols = st.selectbox('Covid metric to view', metrics)
#Esto espara hacer una tabla 
#def get_table():
#    datatable = df[['state', 'confirmed', 'recovered', 'deaths','active']].sort_values(by=['confirmed'], ascending=False)
#    datatable = datatable[datatable['state'] != 'State Unassigned']
#    return datatable

#datatable = get_table()
#st.markdown("### Covid-19 cases in India")
#st.markdown("The following table gives you a real-time analysis of the confirmed, active, recovered and deceased cases of Covid-19 pertaining to each state in India.")
#st.dataframe(datatable) # will display the dataframe
#st.table(datatable)# will display the table