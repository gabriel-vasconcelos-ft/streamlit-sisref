import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/edit#gid=1378939680' 
#df = pd.read_csv(url)
#st.write(df)

filename = "relatorio-sisref-sad-relatorio-sisref-sad.csv"
st.dataframe(pd.read_csv(filename))


