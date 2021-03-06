# -*- coding: utf-8 -*-
"""Cópia de TemplateProjetoFinal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JIx33OcxV0KCDRX20w-PII0b_rDLT2Sf

Projeto Final de BCC

**Grupo:**

MONIQUE FERREIRA SOUZA; 11202020261; monique.ferreira@aluno.ufabc.edu.br; TNC4BIS0005-15SA (2020.2 - 2N34)

YAGO AUGUSTO MAGALHAES PALMEIRA; 11202021565; yago.augusto@aluno.ufabc.edu.br; TNC4BIS0005-15SA (2020.2 - 2N34)

LARISSA SANTOS COSTA; 11202021759; costa.larissa@aluno.ufabc.com.edu.br; TDC7BIS0005-15SA (2020.2 - 2M34)


**Objetivo do Projeto:**

Este projeto tem como objetivo analisar os dados de vendas dos jogos da Nintendo entre 1983 e 2016. A base de dados que utilizamos contém as colunas NA_Sales, EU_Sales, JP_Sales, Other_Sales e Global_Sales, que significam, respectivamente, vendas na América do Norte, vendas na Europa, vendas no Japão, vendas em outros países fora deste eixo e vendas totais. A base também contém os jogos lançados por ano, plataforma e gênero.
A base original (https://www.kaggle.com/sidtwr/videogames-sales-dataset) contém diversas empresas, porém utilizamos apenas os dados da Nintendo).

**Conceitos aprendidos e utilizados no projeto:**

Conceitos utilizados: ordenação de dados, alteração de tipo de dado, condicional if e else, histograma, input, correlação, correlação Pearson, gráfico de dispersão.


*   Manipulação de Base de Dados
*   Representação Gráfico de Funções
*   Estatística Descritiva
*   Correlação e Regressão
*   ~Programação Sequencial~
*   Programação Condicional
*   ~Estruturas de Repetição~


https://drive.google.com/file/d/1q94JioNusQDAl339X18XCJ5z94UWMx58/view?usp=sharing

Por favor, na célula acima, deixem apenas as informações pedidas. O projeto de vocês deve começar a partir desta célula. A partir daqui, vocês podem misturar e combinar células de texto e código. 

Sempre expliquem o que cada célula está fazendo, seja por meio de texto ou por meio de comentários no código. Por exemplo:
"""

# Commented out IPython magic to ensure Python compatibility.
#Importando as bibliotecas que utilizaremos
 
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

#Importando a base de dados "nintendovendas"
 
codigo = "10qthfMJKz_WVtXUzvM-W3NljNzJ7Xr8p" #Id do arquivo
file = "https://drive.google.com/u/3/uc?id=" + codigo + "&export=download"
 
df = pd.read_csv(file, sep = ",") #Lendo os dados e separando em colunas
df.head() #Mostrando o cabeçalho dos dados

"""Os dados estão naturalmente ordenados em ordem decrescente na coluna Global_Sales, vamos descobrir quais jogos foram líderes em vendas fora do eixo NA, EU e JP."""

other_sales = df.sort_values(by="Other_Sales", ascending=False) #Ordenando em ordem decrescente
other_sales = other_sales.head() #Para exibir somente o cabeçalho
print(other_sales) #Print desse cabeçalho

"""Quais jogos foram lançados no ano do seu nascimento?"""

#Primeiro vamos transformar os dados da coluna Year de string para int
x = df.Year
map(int, x)
 
#Solicitando a informação para o usuário
ano = int(input("Digite o ano do seu nascimento com 4 dígitos: "))
if ano <1983:
  print("Nossos dados são somente a partir de 1983, desculpe!")
else:
  filtroAno = df[df["Year"] == ano] #Filtrando o ano
  print(filtroAno['Name'])
  contador = filtroAno.count()
  print("\nForam lançados",contador['Name'], "jogos no ano do seu nascimento.")

"""  Demonstrando graficamente as regiões que tiveram o maior número de vendas de acordo com cada ano."""

#plt.plot(x,y)
s = 0.2
p = 0.10
plt.bar(df.Year + s, df.NA_Sales , label='America do Norte')
plt.bar(df.Year - s, df.EU_Sales ,label='Europa')
plt.bar(df.Year + p, df.JP_Sales ,label='Japao')
plt.bar(df.Year - p, df.Other_Sales ,label='Others')
plt.legend()

#Permite ao usuário escolher as regiões separadamente para analisar o gráfico do número de vendas por ano
pais = input("Qual região quer analisar? Escolha entre: Japao, Europa, Outros e America do norte: ")
if (pais=="Japao"):
  plt.bar(df.Year , df.JP_Sales ,label='Japao')
  plt.legend()
elif (pais=="Europa"):
    plt.bar(df.Year , df.EU_Sales ,label='Europa')
    plt.legend()
elif (pais=="Other" or pais.lower=="Outros"):
    plt.bar(df.Year , df.Other_Sales ,label='Outros Países')
    plt.legend()
elif (pais=="America do Norte"):
    plt.bar(df.Year , df.NA_Sales ,label='America do Norte')
    plt.legend()

#Mostrando o cabeçalho dos dados
df = pd.read_csv(file)

#Criando uma variável para analisar apenas a quantidade de jogos vendidos na América do Norte e a quantidade de jogos vendidos no mundo
df1 = df[['NA_Sales','Global_Sales']]

df1.columns = ("JOGOS VENDIDOS AMÉRICA N","JOGOS VENDIDOS NO MUNDO") #RENOMEEI 

sns.set() #COLOQUEI LINHAS DE GRADE
df1.plot(subplots = True, figsize=(22,8)) #PRIMEIRO ANALISEI OS DADOS EM GRÁFICOS DIFERENTES E SELECIONEI O TAMANHO

"""Já é possível perceber um alto nível de correlação"""

#Coeficiente de Correlação de Pearson
#índice de correlação entre a quantidade de vendas de jogos na América do Norte e no mundo
sns.heatmap(df1.corr(), annot=True)

#Gráfico de dispersão
df = pd.read_csv(file)
plt.plot(df["NA_Sales"], df["Global_Sales"],'.')

"""Conclusão: As variáveis estão diretamente correlacionadas."""