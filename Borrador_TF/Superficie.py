#SUPERFICIE FORESTAL DENTRO DE AREAS PROTEGIDAS
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('data.csv',delimiter=';',encoding='latin-1')
data=pd.DataFrame(df)
df=data.set_index('Pais')
#Superfie forestal dentro de areas protegidas por PERIODOS


def super_proteg_x_period(df):
    sup_prot=df[['Continente','Deforestacion','Periodos','Superficie_areas_protegidas']]
    sup_x_periodo=pd.DataFrame({'SupF_proteg':sup_prot.groupby('Periodos')['Superficie_areas_protegidas'].sum()}).reset_index()
    print(sup_x_periodo)
    print()
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 1:\n\n")
    print("Respecto al intervalo de anio 2000-2010, la Superficie Forestal dentro de Areas protegidas a ",)
    print("nivel global fue aproximadamente 673 574.190 hectareas por anio. En el siguiente periodo se ")
    print("presento una considerada disminucion del indicador, en unas 15 218.862 hectareas. Sin ")
    print("embargo, en el ultimo periodo el incremento supero las cifras iniciales, ya que se registraron ")
    print("697 545.530 hectareas dentro de superficies protegidas, es decir, un aumento del 3%. Se espera ")
    print("que este valor guarde relacion con el intento de las organizaciones por mitigar la deforestacion ")      
    print("global.")
    print()     
    periodos=['2000-2010','2010-2015','2015-2020']
    plt.plot(periodos,sup_x_periodo['SupF_proteg'])
    plt.ylabel('Superficie Forestal Protegida en 1000 hec/anio')
    plt.xlabel('Periodos')
    plt.title('Superficie Forestal protegida por periodos')
    plt.show()

#SUPERF. FORES. AREAS PROT PROMEDIO POR CONTINENTE

def super_x_period_x_conti(df):
    sup_prot=df[['Continente','Deforestacion','Periodos','Superficie_areas_protegidas']]
    sup_conti_anio=pd.DataFrame({'SupF_proteg':sup_prot.groupby(['Continente','Periodos'])['Superficie_areas_protegidas'].mean()}).reset_index()
    print(sup_conti_anio)
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 3:\n\n")
    print("En la grafica podemos observar que America se ha mantenido constante en el alto indice de",)
    print("superficie forestal protegida, a su vez, Europa muestra el mismo comportamiento con cifras,en")
    print("el periodo 2000-2010 de 1452.17 1000 hectareas/anio aproximadamente, siendo este el")
    print("numero mas bajo en los ultimos 20 anios. Sin embargo, ha ido incrementando este indicador, ya")
    print("que se muestra actualmente un cambio que representa el 23.46% respecto al primer periodo.")
    print("Asimismo, se observa incertidumbre en los datos obtenidos de Africa y Oceania. Por otro lado,")      
    print("Asia ha presentado una reduccion de 323.72 en 1000hectareas durante el intervalo de 2015-")
    print("2020, a pesar de mostrarse constante los periodos previos. En conclusión, se sugiere realizar una ")
    print("investigación profunda a los posibles motivos internos de una disminucion en las superficies ")
    print("protegidas por cada nacion asiática. Si bien America sigue liderando el estudio, debe progresar")
    print("con sus politicas ambientales para prevenir el impacto de factores externos.")
    print() 
    #PARA SACAR PROMEDIO DE SUPERFICIE POR PERIODO DE CADA CONTINENTE
    #AFRICA
    africa_A=sup_conti_anio['SupF_proteg'][0]
    africa_B=sup_conti_anio['SupF_proteg'][1]
    africa_C=sup_conti_anio['SupF_proteg'][2]
    #AMERICA
    america_A=sup_conti_anio['SupF_proteg'][3]
    america_B=sup_conti_anio['SupF_proteg'][4]
    america_C=sup_conti_anio['SupF_proteg'][5]
    #ASIA
    asia_A=sup_conti_anio['SupF_proteg'][6]
    asia_B=sup_conti_anio['SupF_proteg'][7]
    asia_C=sup_conti_anio['SupF_proteg'][8]
    #EUROPA
    europa_A=sup_conti_anio['SupF_proteg'][9]
    europa_B=sup_conti_anio['SupF_proteg'][10]
    europa_C=sup_conti_anio['SupF_proteg'][11]
    #OCEANIA
    oceania_A=sup_conti_anio['SupF_proteg'][12]
    oceania_B=sup_conti_anio['SupF_proteg'][13]
    oceania_C=sup_conti_anio['SupF_proteg'][14]

    list_A=[africa_A,america_A,asia_A,europa_A,oceania_A]
    list_B=[africa_B,america_B,asia_B,europa_B,oceania_B]
    list_C=[africa_C,america_C,asia_C,europa_C,oceania_C]
       
    contis=['Africa','America','Asia','Europa','Oceania'] #columa 1
    nuevo_data=pd.DataFrame({'Continente':contis,'2000-2010':list_A,'2010-2015':list_B,'2015-2020':list_C}) #diccionario
    nuevo_data=nuevo_data.set_index('Continente')
    nuevo_data.plot(kind='bar',legend='Reverse')
    plt.title('Promedio Superficie Forestal Protegida por periodo')
    plt.xlabel('Continentes')
    plt.grid()
    plt.show()



def Comparar_def_y_super_proteg(df):
    sup_prot=df[['Deforestacion','Periodos','Superficie_areas_protegidas']]
    sup_prot=sup_prot[sup_prot['Superficie_areas_protegidas']<10000]
    sup_prot1=sup_prot[sup_prot["Periodos"]=='A']
    sup_prot2=sup_prot[sup_prot["Periodos"]=='B']
    sup_prot3=sup_prot[sup_prot["Periodos"]=='C']
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 4:\n\n")
    print("Se puede observar en el primer periodo una tendencia alta en las cifras de la deforestacion, ")
    print("y, ante ello, la mayoría de las naciones con los indices mas altos presentaron una mínima . ")
    print("superficie forestal dentro de áreas protegidas. Respecto al periodo 2010-2020, se visualiza")
    print("una disminucion ligera de la deforestacion y mayor alcance las areas protegidas por los paises ")
    print("que previamente se encontraban en un punto medio, Por ultimo, se muestra nuevamente un incremento ")      
    print("en la deforestacion; no obstante, la dispersión de las naciones ,en sentido de la superficie protegida,")
    print("ha demostrado inclinarse progresivamente a la incorporacion de areas verdes. Se espera un")
    print("avance en politicas ambientales que optmicen estos datos y reduzcan los efecto de la ") 
    print("perdida de zonas forestales.")
    fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharex=True ,sharey=True)
    axs[0].scatter(sup_prot1['Deforestacion'],sup_prot1['Superficie_areas_protegidas'],c='red')
    axs[0].set_xlabel('Deforestacion 2000-2010')
    axs[1].scatter(sup_prot2['Deforestacion'],sup_prot2['Superficie_areas_protegidas'],c='green')
    axs[1].set_xlabel('Deforestacion 2010-2015')
    axs[2].scatter(sup_prot3['Deforestacion'],sup_prot3['Superficie_areas_protegidas'],c='blue')
    axs[2].set_xlabel('Deforestacion 2015-2020')
    fig.suptitle('Comparacion Deforestacion y Superficie Protegida en 1000 hectareas')
    fig.supylabel('Superficie Protegida')
    plt.show()


#Promedio x continente:
def super_prom_proteg_x_conti(df):
    sup_prot=df[['Continente','Deforestacion','Periodos','Superficie_areas_protegidas']]
    sup_prom_conti=pd.DataFrame({'SupF.prom':sup_prot.groupby('Continente')['Superficie_areas_protegidas'].mean()})
    print(sup_prom_conti)
    print()
    print("ANALISIS: ")
    print()
    print("Grafico 2:\n\n")
    print("Segun la grafica, se puede observar que el continente Americano ha obtenido el mayo promedio ",)
    print("de superficie forestal protegida, con una cifra de 2 566.05 aproximadamente. En contraste, el ")
    print("continente europeo no ha logrado entrar estos ultimos anios a la barrera de las 2000 hectareas. ")
    print("En conclusion, se espera en los proximos analisis encontrar que el continente Americano ha ")
    print("estado disminuyendo sus índices de deforestacion, respecto a los intervalos de tiempo. Por otro ")
    print("lado, surge la necesidad de concientizar a la comunidad europea para fomentar la creacion de ")      
    print("areas protegidas y reducir las cifras de perdida forestal.")
    print() 
    sup_prom_conti.plot(kind='bar',color='y')
    plt.title("Promedio Superficie Forestal dentro de Areas protegidas")
    plt.show()

#super_proteg_x_period(df)
#super_prom_proteg_x_conti(df)
#Comparar_def_y_super_proteg(df)
#super_x_period_x_conti(df)



