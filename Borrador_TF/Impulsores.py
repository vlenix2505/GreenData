import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("data.csv",encoding = 'latin-1',delimiter=';',usecols=['Continente','Deforestacion','Impulsores_deforestacion'])
df=pd.DataFrame(data)

def Impulsador_mas_repitente_x_continente():
    data = pd.read_csv("data.csv",encoding = 'latin-1',delimiter=';',usecols=['Continente','Deforestacion','Impulsores_deforestacion'])
    df=pd.DataFrame(data)
    rango=len(df.axes[0])
    constante=1
    impulsador_africa=0.00
    impulsador_america=0.00
    impulsador_asia=0.00
    impulsador_europa=0.00
    impulsador_oceania=0.00
    for i in range(0,rango):
        if df.loc[i,'Impulsores_deforestacion']==4 and df.loc[i,'Continente']=='Africa':
           impulsador_africa+=constante
        if df.loc[i,'Impulsores_deforestacion']==4 and df.loc[i,'Continente']=='Asia':
           impulsador_asia+=constante
        if df.loc[i,'Impulsores_deforestacion']==4 and df.loc[i,'Continente']=='America':
           impulsador_america+=constante
        if df.loc[i,'Impulsores_deforestacion']==4 and df.loc[i,'Continente']=='Europa':
           impulsador_europa+=constante
        if df.loc[i,'Impulsores_deforestacion']==4 and df.loc[i,'Continente']=='Oceania':
           impulsador_oceania+=constante
       
    fig, ax = plt.subplots()
    continentes = ['Africa', 'America', 'Asia', 'Europa' , 'Oceania']
    counts = [impulsador_africa, impulsador_america, impulsador_asia, impulsador_europa, impulsador_oceania]
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:cyan']
    ax.bar(continentes, counts, color=bar_colors)

    ax.set_ylabel('Frecuencia')
    ax.set_title('Sobreexplotacion por lena- Analisis cada continente')
    
    #Reporte
    print("ANALISIS")
    print()
    print("Grafico 2:\n\n")
    print("La Sobreexplotacion para obtener lena, es el impulsor que mas se repite a nivel mundial. Hemos")
    print("desglozado la informacion del impulsor para ver en que continente resulto mas perjudicial.  ")
    print("En la grafica podemos apreciar que Africa ha sido el continentes que mas se afecto por el")
    print("factor, presentando una marcada diferencia con las demas areas.")
    print()
    plt.show()


def Impulsadores_totales():    
    data = pd.read_csv("data.csv",encoding = 'latin-1',delimiter=';',usecols=['Continente','Deforestacion','Impulsores_deforestacion'])
    df=pd.DataFrame(data)
    rango=len(df.axes[0])
    constante=1
    impulsador1=0.00
    impulsador2=0.00
    impulsador3=0.00
    impulsador4=0.00
    impulsador5=0.00
    impulsador6=0.00
    impulsador7=0.00
    impulsador8=0.00
    for i in range(0,rango):
        if df.loc[i,'Impulsores_deforestacion']==1:
            impulsador1+=constante
        if df.loc[i,'Impulsores_deforestacion']==2:
            impulsador2+=constante
        if df.loc[i,'Impulsores_deforestacion']==3:
            impulsador3+=constante
        if df.loc[i,'Impulsores_deforestacion']==4:
            impulsador4+=constante
        if df.loc[i,'Impulsores_deforestacion']==5:
            impulsador5+=constante
        if df.loc[i,'Impulsores_deforestacion']==6:
            impulsador6+=constante
        if df.loc[i,'Impulsores_deforestacion']==7:
            impulsador7+=constante
        if df.loc[i,'Impulsores_deforestacion']==8:
            impulsador8+=constante
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 1:\n\n")
    print("La frecuencia que se repite cada impulsador es constante. El  que mas")
    print("se repite es el 4 que viene a ser la Sobreexplotacion para obtener lena, con una")
    print("aparicion de 85 veces en en los diferentes peripdos del 2000 al 2020. Esto es preocupante, ya que   ")
    print("las poblaciones aledanas a bosques que no cuentan con calefaccion o una cocina a gas")
    print("para  sobrevivir, deciden depender unicamente de los recursos de la naturaleza, sin ")
    print("saber que el consumo masivo a estos afecta al mundo.")
    print()
    fig, ax = plt.subplots()
    periodos = ['1', '2', '3', '4' , '5' , '6' , '7' , '8']  
    numeros = [impulsador1, impulsador2, impulsador3, impulsador4,impulsador5,impulsador6,impulsador7,impulsador8]
    bar_colors = ['tab:blue']*8
    ax.bar(periodos, numeros, color=bar_colors)
    ax.set_title('Frecuencia de impulsadores de la deforestacion 2000-2020')
    plt.show()

def Media_impulsadores(df):
    imp=df[['Impulsores_deforestacion','Deforestacion','Periodos']]
    imp1=imp[imp['Periodos']=='A']
    imp2=imp[imp['Periodos']=='B']
    imp3=imp[imp['Periodos']=='C']
    print()
    print("ANALISIS")
    print()
    print("Grafico 3:\n\n")
    print("En el periodo de 2010-2015 (grafica del medio) podemos apreciar que la media de cada impulsor  ")
    print("de la deforestacion es mas imponente a que en otros peiodos, ya que la mayoria se mantienen ")
    print("en los limites. ")
    print()
    fig, (ax1,ax2,ax3)=plt.subplots(nrows=1,ncols=3)
    ax1.violinplot(imp1['Impulsores_deforestacion'],showmedians=True)
    ax1.set_xlabel('2000-2010')
    ax2.violinplot(imp2['Impulsores_deforestacion'],showmedians=True)
    ax2.set_xlabel('2000-2010')
    ax3.violinplot(imp3['Impulsores_deforestacion'],showmedians=True)
    ax3.set_xlabel('2000-2010')
    fig.suptitle('Distribucion de los impulsores en cada periodo')
    fig.supylabel('Impulsores(1-8)')
    plt.show()

      