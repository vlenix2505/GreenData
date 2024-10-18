import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv',delimiter=';',encoding='latin-1')
data=pd.DataFrame(df)
df=data.set_index('Pais')
expa=df[['Continente','Periodos','Expansion','Superficie_areas_protegidas']]


#print(expa)
#EXPANSION TOTAL POR CONTINENTE EN TODOS PERIODOS

def expa_x_continente(df):
    expa=df[['Continente','Periodos','Expansion','Superficie_areas_protegidas']]
    expa_x_continente=expa.groupby('Continente')['Expansion'].sum()
    print(expa_x_continente)
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 2:\n\n")
    print("Del total de la Expansion Forestal en 1000 hectareas/anio desde el anio 2010 hasta el 2020, el continente",)
    print("que ha registrado mayor porcentaje es Asia, con un 48.0%. El siguiente 42.1% corresponde a America, Asia")
    print(" y Africa en conjunto. finalmente, entre 2015-2020 se muestra una deficiente expansion, con 8 404.36 1hectareas")
    print("por anio. Es decir, durante los ultimos 20 anios la expansion forestal total ha disminuido en 4647.07 hectareas")
    print("por anio. En consecuencia, las organizaciones mundiales deben implementar politicas necesarias ambientales para")
    print("contrarrestar la situacion, pues la abundancia de arboles es esencial para la vida silvestre y otras actividades")      
    print("biologicas del entorno.")
    print()     
    expa_x_continente.plot.pie(autopct="%1.1f%%")
    plt.ylabel(' ')
    plt.title('Expansion Forestal Total 2010-2020')
    plt.show()


#AGRUPANDO POR PERIODOS EXPANSION TOTAL
def expa_x_period(df):
    expa=df[['Continente','Periodos','Expansion']]
    expa_x_anio=pd.DataFrame({'ExpaTotal': expa.groupby('Periodos')['Expansion'].sum()}).reset_index()
    print(expa_x_anio)
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 1:\n\n")
    print("Respecto al intervalo de anio 2000-2010, la expansion forestal total fue de 13 051.43 hectareas por anio,en",)
    print("el periodo 2010-2015 este indicador presento un descenso considerable, culminando el ciclo con 10 220.64")
    print("hectareas por anio; finalmente, entre 2015-2020 se muestra una deficiente expansion, con 8 404.36 hectareas")
    print("por anio. Es decir, durante los ultimos 20 anios la expansion forestal total ha disminuido en 4647.07 hectareas")
    print("por anio. En consecuencia, las organizaciones mundiales deben implementar politicas necesarias ambientales para")
    print("contrarrestar la situacion, pues la abundancia de arboles es esencial para la vida silvestre y otras actividades")      
    print("biologicas del entorno.")
    print()
    #Eje X y Eje Y
    anios=['2000-2010','2010-2015','2015-2020']
    plt.plot(anios,expa_x_anio['ExpaTotal'])
    plt.ylabel('Expansion Forestal Total en 1000 hec/anio)')
    plt.xlabel('Periodos')
    plt.title('Expansion Forestal por periodo de tiempo')
    plt.show()
    


#AGRUPANDO EXPANSION TOTAL POR CONTINENTE Y PERIODO
#Primero CONTINENTES, LUEGO PERIODOS , FINAL EXPANSION TOTAL
#Arreglar America
def expa_conti_period(df):
    expa=df[['Continente','Periodos','Expansion']]
    expa_conti_x_anio=pd.DataFrame({'ExpaTotalProm': expa.groupby(['Continente','Periodos'])['Expansion'].mean()}).reset_index()
    print(expa_conti_x_anio)
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 3:\n\n")
    print("Segun la grafica, se puede visualizar el punto minimo entre todos los intervalos de tiempo en el",)
    print("periodo 2015-2020 correspondiente al continente europeo, con un promedio de 16.87 en 1000")
    print("hectareas por anio. Por otro lado, el pico de la representacion esta en el intervalo 2000-2010,")
    print("respecto al continente asiatico, con una cifra de 129.64 en 1000 hectareas por anio. Asimismo,")
    print("es importante mostrar atención a la disminución de la expansión en América, ya que las cifras ")
    print("han variado en 47.64 puntos en los ultimos 20 anios. Por ello, se recomienda a las instituciones")
    print("ambientales implementar planes de gestion forestal a largo plazo para contrarrestar las cifras")      
    print("presentadas y enfrentarse a la deforestacion, pues en esta zona se encuentra la Amazonia, el")
    print("cual presenta mas de 3615 de especies de arboles en sus humedales.")
    print()
    conti=expa_conti_x_anio[expa_conti_x_anio['Continente']=='Asia']
    anios=['2000-2010','2010-2015','2015-2020']
    y_asia=conti['ExpaTotalProm']
    conti=expa_conti_x_anio[expa_conti_x_anio['Continente']=='America']
    y_ame=conti['ExpaTotalProm']
    conti=expa_conti_x_anio[expa_conti_x_anio['Continente']=='Africa']
    y_afrik=conti['ExpaTotalProm']
    conti=expa_conti_x_anio[expa_conti_x_anio['Continente']=='Europa']
    y_eu=conti['ExpaTotalProm']
    conti=expa_conti_x_anio[expa_conti_x_anio['Continente']=='Oceania']
    y_ocea=conti['ExpaTotalProm']
    plt.plot(anios,y_asia,'c--',label="Asia")
    plt.plot(anios,y_ame,'y-',label="America")
    plt.plot(anios,y_afrik,'ro-',label="Africa")
    plt.plot(anios,y_eu,'bs-',label="Europa")
    plt.plot(anios,y_ocea,label="Oceania")  
    plt.legend()
    plt.ylabel('Expansion Forestal Promedio en 1000 hec/anio')
    plt.xlabel('Periodos')    
    plt.show()

###EXPANSION TOTAL PROMEDIO DE TODOS PERIODOS X PAIS 
#expa_x_pais=data[['Pais','Periodos','Expansion']]
#expa_x_pais=pd.DataFrame({'ExpaTotalProm':expa_x_pais.groupby('Pais')['Expansion'].mean()}).reset_index()

##EXPANSION TOTAL PROMEDIO DE TODOS PERIODOS TODOS PAISES
#prom=expa_x_pais['ExpaTotalProm'].mean()

#5 PAISES CON MAYOR EXPANSION PROM TOTAL
def Maximos_cinco_periodo(expa_x_pais,prom):
    expa_x_pais=expa_x_pais.set_index('Pais')
    maxis=expa_x_pais[expa_x_pais['ExpaTotalProm']>prom]
    maxis=maxis.sort_values(by='ExpaTotalProm',ascending=False,ignore_index=False)
    print(maxis.head(10))
    maxis=maxis.head(10).plot(kind='barh',legend='Reverse')
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 4:\n\n")
    print("En la grafica se puede visualizar que el pais con la mayor expansion forestal al promedio es China, ",)
    print("con hectareas por anio. Los demas paises completan el podio con cifras menores a 1000 ")
    print("hectareas por anio. Por ello, se espera que el pais asiatico presente una alta cifra de Superficie ")
    print("respecto al continente asiatico, con una cifra de 129.64 en 1000 hectareas por anio. Asimismo,")
    print("han variado en 47.64 puntos en los ultimos 20 anios. Por ello, se recomienda a las instituciones")
    print("ambientales implementar planes de gestion forestal a largo plazo para contrarrestar las cifras")      
    print("presentadas y enfrentarse a la deforestacion, pues en esta zona se encuentra la Amazonia, el")
    print("cual presenta mas de 3615 de especies de arboles en sus humedales.")
    print()
    plt.title('Top 10 paises Expansion mayor al promedio')
    plt.ylabel('Paises')
    plt.xlabel('Promedio en 1000 hect/anio')
    plt.show()



#expa_x_continente(df)
#expa_x_period(df)
#expa_conti_period(df)
#Maximos_cinco_periodo(expa_x_pais,prom)





