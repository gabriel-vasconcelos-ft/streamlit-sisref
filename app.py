import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/edit#gid=1378939680' 
#df = pd.read_csv(url)
#st.write(df)

filename = "relatorio-sisref-sad-relatorio-sisref-sad.csv"
df = pd.read_csv(filename)
st.dataframe(df)


#Contagem de Refeições
contagem_refeicoes = df['Refeicao'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=contagem_refeicoes.index, y=contagem_refeicoes.values)
plt.xlabel('Tipo de Refeição')
plt.ylabel('Contagem')
plt.title('Contagem de Refeições por Tipo')
plt.xticks(rotation=30)
st.pyplot()


