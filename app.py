import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textwrap import wrap


#url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/edit#gid=1378939680' 
#df = pd.read_csv(url)
#st.write(df)

filename = "relatorio-sisref-sad-relatorio-sisref-sad.csv"
df = pd.read_csv(filename)
st.dataframe(df)


#Contagem de Refeições
ctg_refeicoes = df['Refeicao'].value_counts()
fig, ax = plt.subplots(figsize=(8,8))
sns.barplot(x=ctg_refeicoes.index, y=ctg_refeicoes.values)
plt.xlabel('Período de Refeição')
plt.ylabel('Contagem')
plt.title('Contagem de refeições por Período')
plt.xticks(rotation=30)
st.pyplot(fig.figure)


#Contagem de reservas por curso
ctg_reservas = df['Curso'].value_counts()
fig, ax = plt.subplots(figsize=(10,10))
sns.barplot(x=ctg_reservas.index, y=ctg_reservas.values)
ax.set_xticklabels(['\n'.join(wrap(label, 20)) for label in ctg_reservas.index])
plt.xlabel('Curso')
plt.ylabel('Reservas')
plt.title('Contagem de reservas por Curso')
plt.xticks(rotation=60)
st.pyplot(fig.figure)


#Quantidade de alunos que compareceram
qtd_comparecer = df['Compareceu'].value_counts()
fig, ax = plt.subplots(figsize=(5,5))
sns.barplot(x=qtd_comparecer.index, y=qtd_comparecer.values)
plt.xlabel('Compareceu')
plt.ylabel('Quantidade')
plt.title('Quantidade de alunos que compareceram')
plt.xticks(rotation=45)
st.pyplot(fig.figure)


#Revervas por dia
rsv_data = df['Data_da_Refeicao'].value_counts()
fig, ax = plt.subplots(figsize=(8,8))
sns.barplot(x=rsv_data.index, y=rsv_data.values)
plt.xlabel('Data')
plt.ylabel('Revervas')
plt.title('Revervas por dia')
plt.xticks(rotation=45)
st.pyplot(fig.figure)
