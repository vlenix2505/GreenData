import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv',delimiter=';',encoding='latin-1')
data=pd.DataFrame(df)
df=data.set_index('Pais')


def emision_prom_conti(df):
    emis = df[["Continente", "Emisiones_CO2"]]
    emis_con = pd.DataFrame({'Promedio Emision': emis.groupby('Continente')['Emisiones_CO2'].mean()})
    print(emis_con)
    print()
    print("ANALISIS:")
    print()
    print("Grafico1: \n\nEn los periodos de datos analizados (2000 al 2020), podemos observar como Asia es el continente con mayor toneladas emitidas de dioxido de carbono(CO2) promedio a causa de la deforestacion.\nAmerica emitio menos de la tercera parte del total del continente asiatico.Esto confirma que Asia es el mayor emisor de polucion en el planeta, principalmente debido al crecimiento exponencial de sus habitantes, asi como el de las industrias. ")
    print()
    #grafico
    fig, ax = plt.subplots()
    continentes=['America','Europa','Asia','Africa','Oceania']
    plt.plot(continentes,emis_con['Promedio Emision'], color='c')
    plt.xlabel('Continentes')
    plt.ylabel('Emisiones CO2 (ton)')
    plt.title('Emisiones promedio de CO2 por continente', fontsize = 15)
    plt.show()


def emision_x_period(df):
    emis = df[["Periodos", "Emisiones_CO2"]]
    emis_con = pd.DataFrame({'Promedio Emision': emis.groupby('Periodos')['Emisiones_CO2'].mean()})
    print(emis_con)
    print()
    print("ANALISIS:")
    print()
    print("Grafico2: \n\nEl grafico 2 muestra una tendencia ascendente respecto a las emisiones de CO2 mundiales, la cual se divide en tres periodos.\nMientras que durante los dos primeros periodos(2000-2010 y 2010-2015)se mantuvo realtivamente estable, \nobservamos un incremento global de emisiones de CO2 en el periodo tres.")
    print()
    x = []
    y = []
    fig, ax = plt.subplots()
    periodos=['2000-2010','2010-2015','2015-2020']
    plt.plot(periodos,emis_con['Promedio Emision'], color='m',linestyle=':', marker='o')
    plt.xlabel('Periodos')
    plt.ylabel('Emisiones de CO2 (ton)')
    plt.title('Emisiones de CO2 por periodo', fontsize = 15)
    plt.show()

def emi_cont_per(df):
    emi=df[['Continente','Periodos','Emisiones_CO2']]
    emi_con=pd.DataFrame({'PromedioEmision': emi.groupby(['Continente','Periodos'])['Emisiones_CO2'].mean()}).reset_index()
    print(emi_con)
    print()
    print("ANALISIS:")
    print()
    print("Grafico3: \n\nEl grafico 3 muestra las emisiones de CO2 por periodo y continente. El eje x divide los tres periodos, y el eje y los promedios de emision de CO2. \nEstos, son representados por el triangulo y un color asignado, el cual esta especificado al continente correspondiente y puede ser visualizado en la leyenda de la grafica. ")
    print()
    conti=emi_con[emi_con['Continente']=='Asia']
    x_todos=conti['Periodos']
    y_asia=conti['PromedioEmision']
    conti=emi_con[emi_con['Continente']=='America']
    y_ame=conti['PromedioEmision']
    conti=emi_con[emi_con['Continente']=='Africa']
    y_afrik=conti['PromedioEmision']
    conti=emi_con[emi_con['Continente']=='Europa']
    y_eu=conti['PromedioEmision']
    conti=emi_con[emi_con['Continente']=='Oceania']
    y_ocea=conti['PromedioEmision']
    plt.plot(x_todos,y_asia,'m^',label="Asia")
    plt.plot(x_todos,y_ame,'g^',label="America")
    plt.plot(x_todos,y_afrik,'r^',label="Africa")
    plt.plot(x_todos,y_eu,'y^',label="Europa")
    plt.plot(x_todos,y_ocea,'b^',label="Oceania")  
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title('Emisiones de CO2 por periodo y continente')
    plt.ylabel('Emisiones C02(ton)')
    plt.xlabel('Periodos')    
    plt.show()

def porcen_emi(df):
    emi=df[['Continente','Periodos','Emisiones_CO2']]
    emi_con=pd.DataFrame({'SumaEmision': emi.groupby(['Continente','Periodos'])['Emisiones_CO2'].sum()}).reset_index()
    print(emi_con)
    print()
    print("ANALISIS:")
    print()
    print("Grafico4: \n\nSegun la grafica circular, observamos las distribuciones de los porcentajes de emsiones de CO2 por continente desde del anio 2000 al 2020. \nCada porcentaje de emisiones es representada por un color representante del continente correspondiente. \nLa leyenda muestra los colores asignados a cada segmento, donde se concluye que Asia es el continente con mayor porcentaje de emisiones con el 32.76% a lo largo de los tres periodos. \n ")
    print()    
    #AFRICA
    africa_A=emi_con['SumaEmision'][0]
    africa_B=emi_con['SumaEmision'][1]
    africa_C=emi_con['SumaEmision'][2]
    suma_afr=africa_A+africa_B+africa_C
    #AMERICA
    america_A=emi_con['SumaEmision'][3]
    america_B=emi_con['SumaEmision'][4]
    america_C=emi_con['SumaEmision'][5]
    suma_am=america_A+america_B+america_C
    #ASIA
    asia_A=emi_con['SumaEmision'][6]
    asia_B=emi_con['SumaEmision'][7]
    asia_C=emi_con['SumaEmision'][8]
    suma_asi=asia_A+asia_B+asia_C
    #EUROPA
    europa_A=emi_con['SumaEmision'][9]
    europa_B=emi_con['SumaEmision'][10]
    europa_C=emi_con['SumaEmision'][11]
    suma_eu=europa_A+europa_B+europa_C
    #OCEANIA
    oceania_A=emi_con['SumaEmision'][12]
    oceania_B=emi_con['SumaEmision'][13]
    oceania_C=emi_con['SumaEmision'][14]
    suma_oc=oceania_A+oceania_B+oceania_C

    values=[suma_afr,suma_am, suma_asi, suma_eu, suma_oc]
    names='Africa','America','Asia','Europa','Oceania'
    suma_tot=suma_afr+suma_am+suma_asi+suma_eu+suma_oc
    por_afr= (suma_afr/suma_tot) * 100
    por_am = (suma_am/suma_tot) * 100
    por_asi = (suma_asi/suma_tot) * 100
    por_eu = (suma_eu/suma_tot) * 100
    por_oc = (suma_oc/suma_tot) * 100
    colors = ['#7F7F7F', '#9467BD', '#8EB897', '#E377C2','#BCBD22']
    ptg= por_afr.round(2), por_am.round(2),por_eu.round(2),por_asi.round(2),por_oc.round(2)
    plt.pie(values,labels=ptg, labeldistance=1.15,wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=colors)
    plt.legend(names,loc='center left', bbox_to_anchor=(1.5, 0.5))
    plt.title('Porcentaje de emisiones promedio de C02(ton) por continente.2000-2020')   
    plt.show()


#emision_prom_conti(df)
#emision_x_period(df)
#emi_cont_per(df)
#porcen_emi(df)