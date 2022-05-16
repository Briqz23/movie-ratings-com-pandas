# -*- coding: utf-8 -*-
"""04_Data_VIsualization

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/Briqz23/7e42c16d09bad5215f591f4d0422cb06/introdu-o-ao-data-science.ipynb
"""

import pandas as pd
tmdb = pd.read_csv("tmdb_5000_movies.csv")
tmdb.head()

#para saber quais são as linguas.
siglas = tmdb["original_language"].value_counts().index  #tmdb.original_language.value_counts().index

#para saber a quantidade para cada lingua distintas
valores = tmdb.original_language.value_counts().values

#for i in range (len(valores)):
  #print (f'{siglas[i].upper()}:{valores[i]}')

#para transformar em um dataframe 'de verdade':
contagem_de_lingua = tmdb["original_language"].value_counts().to_frame()
#agora com um index 
contagem_de_lingua = tmdb.original_language.value_counts().to_frame().reset_index()
#renomeando atributos..
contagem_de_lingua.columns = ["idioma_original", "total"]
print (contagem_de_lingua)

#https://seaborn.pydata.org/tutorial/categorical.html


sns.barplot(x = "idioma_original", y = "total", data = contagem_de_lingua)

!pip install seaborn==0.9.0
import seaborn as sns

import matplotlib.pyplot as plt

plt.pie(contagem_de_lingua['total'], labels = contagem_de_lingua.idioma_original)
total_por_lingua = tmdb["original_language"].value_counts()
total_por_lingua.loc["en"]

"""#Comparando ENG VS Todos os outros idiomas"""

total_por_lingua = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)

dados = {
    'lingua' : ['ingles','outros'],
    'total' : [total_de_ingles, total_do_resto]

}

pd.DataFrame(dados)

sns.barplot(data = dados, x = 'lingua', y = 'total')

filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en' ").original_language.value_counts()

sns.catplot(x = "original_language", kind="count", data = filmes_sem_lingua_original_em_ingles)