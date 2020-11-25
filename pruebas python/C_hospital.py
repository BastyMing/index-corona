#-*- coding:utf-8 -*
import streamlit as st
import pandas as pd

capUci=pd.read_csv('CamasUci.csv',header=0)
print (capUci)

st.dataframe(capUci.head())