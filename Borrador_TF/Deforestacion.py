import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #graficar
import io
import xml.etree.ElementTree as ET
from matplotlib.patches import Shadow
data = pd.read_csv("data.csv",encoding = 'latin-1',delimiter=';',usecols=['Continente','Deforestacion','Periodos','Impulsores_deforestacion'])
df=pd.DataFrame(data)

def Deforestacion_por_periodos_continentes(df):
    rango=len(df.axes[0])
    periodoA_america=0.00
    periodoB_america=0.00
    periodoC_america=0.00
    periodoA_asia=0.00
    periodoB_asia=0.00
    periodoC_asia=0.00
    periodoA_africa=0.00
    periodoB_africa=0.00
    periodoC_africa=0.00
    periodoA_europa=0.00
    periodoB_europa=0.00
    periodoC_europa=0.00
    periodoA_oceania=0.00
    periodoB_oceania=0.00
    periodoC_oceania=0.00
    for i in range(0,rango):
      if df.loc[i,'Periodos']=='A' and df.loc[i,'Continente']=='America':
        periodoA_america+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='B' and df.loc[i,'Continente']=='America':
        periodoB_america+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='C' and df.loc[i,'Continente']=='America':
        periodoC_america+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='A' and df.loc[i,'Continente']=='Asia':
        periodoA_asia+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='B' and df.loc[i,'Continente']=='Asia':
        periodoB_asia+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='C' and df.loc[i,'Continente']=='Asia':
        periodoC_asia+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='A' and df.loc[i,'Continente']=='Africa':
        periodoA_africa+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='B' and df.loc[i,'Continente']=='Africa':
        periodoB_africa+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='C' and df.loc[i,'Continente']=='Africa':
        periodoC_africa+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='A' and df.loc[i,'Continente']=='Europa':
        periodoA_europa+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='B' and df.loc[i,'Continente']=='Europa':
        periodoB_europa+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='C' and df.loc[i,'Continente']=='Europa':
        periodoC_europa+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='A' and df.loc[i,'Continente']=='Oceania':
        periodoA_oceania+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='B' and df.loc[i,'Continente']=='Oceania':
        periodoB_oceania+=df.loc[i,'Deforestacion']
      if df.loc[i,'Periodos']=='C' and df.loc[i,'Continente']=='Oceania':
        periodoC_oceania+=df.loc[i,'Deforestacion']
    year = ["2000-2010", "2010-2015", "2015-2020"]
    deforestacion_by_continent = {
        'Africa': [periodoA_africa,periodoB_africa,periodoC_africa],
        'America': [periodoA_america,periodoB_america,periodoC_america],
        'Asia': [periodoA_asia,periodoB_asia,periodoC_asia],
        'Europa': [periodoA_europa,periodoB_europa,periodoC_europa],
        'Oceania': [periodoA_oceania,periodoB_oceania,periodoC_oceania],
    }
    fig, ax = plt.subplots()
    ax.stackplot(year, deforestacion_by_continent.values(),
                 labels=deforestacion_by_continent.keys(), alpha=0.8)
    ax.legend(loc='upper right')
    ax.set_title('Deforestacion')
    ax.set_xlabel('Periodos')
    ax.set_ylabel('Deforestacion en 1000 hectareas por anio')    
    print()
    print("ANALISIS:")
    print()
    print("Grafico 1:\n\n")
    print("Del total de la Deforestacion en 1000 hectareas/anio, se pude apreciar que ")
    print("en el periodo 2000-2010 fue donde se registraton los mas altos indices en todos los continentes.")
    print("Por otro lado, en el periodo 2010-2015 se pudo ver, en ciertos continentes,  ")
    print("una baja considerable en los numeros, hecho que posiblemente fue generado por la prevalencia de ")
    print("la tala indiscriminada. Sin embargo, en el ultimo periodo, la deforestacion volvio a incrementar. ")
    print("Es decir, en los ultimos 5 anios, la deforestacion esta empezando a consolidarse y se estima superar")
    print("las cifras del primer periodo. En consecuencia las Organizaciones mundiales deben empezar a implementar")
    print("politicas, realizar pactos y tratados con el objetivo de afrontar la situacion venidera")   
    print()
    plt.show()

def grafico_barras_deforestacion(df):
    rango=len(df.axes[0])
    numeros_africa=0.00
    numeros_asia=0.00
    numeros_america=0.00
    numeros_europa=0.00
    numeros_oceania=0.00
    for i in range(0,rango):
      if df.loc[i,'Continente']=='Africa':
        numeros_africa+=df.loc[i,'Deforestacion']
      if df.loc[i,'Continente']=='Asia':
        numeros_asia+=df.loc[i,'Deforestacion']
      if df.loc[i,'Continente']=='America':
        numeros_america+=df.loc[i,'Deforestacion']
      if df.loc[i,'Continente']=='Europa':
        numeros_europa+=df.loc[i,'Deforestacion']
      if df.loc[i,'Continente']=='Oceania':
        numeros_oceania+=df.loc[i,'Deforestacion']     
    fig, ax = plt.subplots()
    continentes = ['Africa', 'Asia', 'America', 'Europa','Oceania']
    numeros = [round(numeros_africa,2),round(numeros_asia,2),round(numeros_america,2),round(numeros_europa,2),round(numeros_oceania,2)]
    co=np.arange(len(numeros)) 
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:pink']
    ax.bar(continentes,numeros,color=bar_colors)
    for i,j in zip(co,numeros):
      ax.annotate(j, xy=(i-0.35,j+150))
    ax.set_ylabel('Hectareas')
    ax.set_title('Deforestacion por Continentes')
    ax.set_xlabel('Continentes')
    print()
    print("ANALISIS")
    print()
    print("Grafico 2:\n\n")
    print("Del total de la Deforestacion en 1000 hectareas/anio, el continente que ha registrado mayor porcentaje")
    print("es America, con un 45.2%. Sus numeros no tienen comparacion con los demas continentes. Esto se debe")
    print("a la causa humana, ya que transforma las tierras forestales para otros usos, como centros comerciales.")
    print("El cambio climatico tambien interviene en este dilema,especialmente por los periodos de sequia mas intensos y ")
    print("la aparicion de incendios forestales. Este fenomeno es una de las principales consecuencias de la deforestacion")
    print("la cual estimula las emisiones de dioxido de carbono en el planeta. Por lo tanto, se deben tomar medidas preventivas")
    print("y armar planes de gestion a corto plazo, pues el problema es inmediato respecto al impacto global")
    print()
    plt.show()

def impulsadores_america_defores(df):
    rango=len(df.axes[0])
    impulsador1=0.00
    impulsador2=0.00
    impulsador3=0.00
    impulsador4=0.00
    impulsador5=0.00
    impulsador6=0.00
    impulsador7=0.00
    impulsador8=0.00
    for i in range(0,rango):
      if df.loc[i,'Impulsores_deforestacion']==1 and df.loc[i,'Continente']=='America':
        impulsador1+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==2 and df.loc[i,'Continente']=='America':
        impulsador2+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==3 and df.loc[i,'Continente']=='America':
        impulsador3+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==4 and df.loc[i,'Continente']=='America':
        impulsador4+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==5 and df.loc[i,'Continente']=='America':
        impulsador5+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==6 and df.loc[i,'Continente']=='America':
        impulsador6+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==7 and df.loc[i,'Continente']=='America':
        impulsador7+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==8 and df.loc[i,'Continente']=='America':
        impulsador8+=df.loc[i,'Deforestacion']

   
    labels = 'Agricultura de subsistencia', 'Agricultura permanente', 'Ganaderia extensiva', 'Sobreexplotacion por lena','Sobreexplotacion por madera','Sobreexplotacion por productos madereros','Infraestructura','Otros'
    sizes = [impulsador1, impulsador2, impulsador3, impulsador4,impulsador5,impulsador6,impulsador7,impulsador8]
    explode = (0, 0, 0, 0.1,0,0,0,0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=[' ']*8, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  
    
    ax1.set_title('Deforestacion en 1000 hectareas/anio por Impulsadores en America')
    ax1.legend(
              title="Impulsadores",
              loc="center left",
              bbox_to_anchor=(1.22, 0.3, 0.5, 1))
    plt.legend(labels=labels)
    print('ANALISIS:')
    print()
    print("Grafico 3:\n\n")
    print("America es el continente que mas sufre esta problematica ambiental, con una cifra de 15238.11 ")
    print("hectareas/anio. Esto se debe a las multiples razones por la cual la gente provoca la perdida de")
    print(" estos, las cuales llamaremos Impulsadores. En el grafico podemos apreciar que son 8 principales (FAO),")
    print("siendo la \"Sobreexplotacion por lena\" el que mas ha generado impactos a nivel forestal.")
    print()
    plt.show()

def pais_mas_defo():
    data = pd.read_csv("data.csv",encoding = 'latin1',delimiter=';',usecols=['Pais','Deforestacion','Impulsores_deforestacion'])
    df=pd.DataFrame(data)
    rango=len(df.axes[0])
    impulsador1=0.00
    impulsador2=0.00
    impulsador3=0.00
    impulsador4=0.00
    impulsador5=0.00
    impulsador6=0.00
    impulsador7=0.00
    impulsador8=0.00
    for i in range(0,rango):
      if df.loc[i,'Impulsores_deforestacion']==1 and df.loc[i,'Pais']=='Brasil':
        impulsador1+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==2 and df.loc[i,'Pais']=='Brasil':
        impulsador2+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==3 and df.loc[i,'Pais']=='Brasil':
        impulsador3+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==4 and df.loc[i,'Pais']=='Brasil':
        impulsador4+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==5 and df.loc[i,'Pais']=='Brasil':
        impulsador5+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==6 and df.loc[i,'Pais']=='Brasil':
        impulsador6+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==7 and df.loc[i,'Pais']=='Brasil':
        impulsador7+=df.loc[i,'Deforestacion']
      if df.loc[i,'Impulsores_deforestacion']==8 and df.loc[i,'Pais']=='Brasil':
        impulsador8+=df.loc[i,'Deforestacion']

     
    labels1 = 'Resto del Mundo', 'Brasil'
    sizes = [39017.56, 8692.8]
    explode = (0, 0.1)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels1, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal') 
    plt.show()

    
    fig, ax = plt.subplots()

    barra_abajo = ['1', '2', '3', '4','5','6','7','8']
    counts = [impulsador1, 0.01, 0.01, impulsador4,0.01,0.01,0.01,impulsador8]
    co=np.arange(len(counts))
    bar_labels = 'Agricultura de subsistencia', 'Agricultura permanente', 'Ganaderia extensiva', 'Sobreexplotacion para obtener lena','Sobreexplotacion por madera de construccion','Sobreexplotacion por productos a base de madera','Infraestructura','Otros'
    bar_colors ='tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:purple','tab:brown','tab:pink','tab:cyan' 

    ax.bar(barra_abajo, counts, label=bar_labels, color=bar_colors)

    for i,j in zip(co, counts):
      ax.annotate(j, xy=(i-0.45,j+50))

    ax.set_ylabel('Hectareas/anio')
    ax.set_title('Impulsadores de la Deforestacion en Brasil')
    print()
    print('ANALISIS')
    print()
    print("Grafico 4:\n\n")
    print("El pais con mas deforestacion es Brasil, ocupando el 18.2% de la deforestacion mundial. Su principal impulsador ")
    print("de la deforestacion es la Sobreexplotacion para obtener lena (barra de color naranja), este impulsador    ")
    print("genera 5129.3 hectarea/anio deforestadas. ")
    print()
    plt.show()
    

   
#pais_mas_defo()
#Deforestacion_por_periodos_continentes(df)
#grafico_barras_deforestacion(df)
#impulsadores_america_defores(df)

