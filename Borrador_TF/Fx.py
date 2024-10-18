import pandas as pd
import matplotlib.pyplot as plt
import Expansion as expa
import Superficie as sup
import Deforestacion as defo
import Emisiones as emi
import Impulsores as impul

def pide_nombre():
    nombre = input("Hola usuario!, Ingresa tu nombre: ")
    return nombre
def pide_anio():
    anio = int(input("Dinos en que anio naciste: "))
    edad = 2022 - anio - 1
    return edad

def pais_pro():
    pais=input("De que pais eres?:")
    return pais

def genero():
    sexo=input("Cual es tu sexo? (M = Masculino, F = Femenino):")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M = Masculino, F = Femenino):")
    return sexo


def welcome():
    print("Bienvenido(a) a ... ")
    print("""
 ____                                    ____               __                
/\  _`\                                 /\  _`\\            /\ \__             
\ \ \L\_\   _ __     __      __     ___ \ \ \/\ \\     __   \ \ ,_\     __     
 \ \ \L_L  /\`'__\ /'__`\  /'__`\ /' _ `\\\ \ \ \ \  /'__`\  \ \ \\/   /'__`\   
  \ \ \/, \\\ \ \/ /\  __/ /\  __/ /\ \/\ \\\ \\ \_\ \/\L\.\_\_ \ \ \_ /\\L\.\\_\_ 
   \ \____/ \\ \_\ \ \____\\ \____\\ \_\ \ \_\\\ \____/\ \__/.\_\ \ \__\\\ \\__/.\_\\
    \/___/   \\/_/  \/____/ \/____/ \/_/\/_/ \\/___/  \/__/\/_/  \/__/ \/__/\/_/                                                                 
   
    
    """)

def ver_perfil(nombre,edad,sexo,pais):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "anios")
    print("Sexo:     ", sexo)
    print("Pais:     ", pais)  
    print("--------------------------------------------------")
    print()

def menu():
    print("Acciones disponibles:")
    print("  1. Creadores y objetivos de GreenData")
    print("  2. Mostrar los datos de perfil")
    print("  3. Actualizar el perfil de usuario")
    print("  4. Mostrar Tabla General")
    print("  5. Mostrar Expansion Forestal")
    print("  6. Mostrar Deforestacion")
    print("  7. Mostrar Emisiones de CO2 por deforestacion")
    print("  8. Mostrar Impulsores de la deforestacion")    
    print("  9. Mostrar Superficie forestal dentro de areas protegidas")    
    print("  0. Salir")
    opcion = int(input("Ingresa una opcion: "))
    while opcion<0 or opcion>9:
        print("Opcion no disponible. Intentalo otra vez.")
        opcion = int(input("Ingresa una opcion: "))
    return opcion

def objetivos():
    print("CREADORES GREEN-DATEROS:")
    print("-Maria Alejandra Lau")
    print("-Belen Ortiz")
    print("-Renzo Diaz")
    print("-Paolo Lopez")
    print()
    print("OBJETIVOS:")
    print("-Greendata se creo con el objetivo de mostrarle a los usuarios reportes de datos analizados respecto  ")
    print("a la deforestacion. Este problema ambiental ha generado impactos negativos en el planeta, por lo que")
    print("surge la necesidad de conocer las causas detras del aumento masivo de perdidas forestales. Es asi que ")
    print("esta aplicacion ha seleccionado 6 indicadores para representar graficamente la situacion mundial y plantear ")
    print("hipotesis sobre las posibles soluciones o medidas que la sociedad debe considerar para un desarrollo sostenible.")
    print()
    print("Te invitamos a seleccionar las opciones de nuestro menu!")
    print()

def tabla_general(df):
    print(df)
    print()

def Expansion_Forestal(data,df):
    #Para Expansion
    expa_x_pais=data[['Pais','Periodos','Expansion']]
    expa_x_pais=pd.DataFrame({'ExpaTotalProm':expa_x_pais.groupby('Pais')['Expansion'].mean()}).reset_index()
    prom=expa_x_pais['ExpaTotalProm'].mean()
    print("Reportes a analizar: ")
    print("1. Expansion total por periodo de tiempo")
    print("2. Expansion total por continente")
    print("3. Expansion total promedio por continente y periodo de tiempo")
    print("4. 10 paises con Expansion Forestal mayor al promedio")
    op = int(input("Ingresa una opcion: "))
    while op<0 or op>4:
        print("Opcion no disponible. Intentalo otra vez.")
        op = int(input("Ingresa una opcion: "))
    if op==1:
        expa.expa_x_period(df)
    elif op==2:
        expa.expa_x_continente(df)        
    elif op==3:
        expa.expa_conti_period(df)
    else:
        expa.Maximos_cinco_periodo(expa_x_pais,prom)

def Superficie_Protegida(df):
    print("Reportes a analizar: ")
    print("1. Superficie Forestal Protegida total por periodo de tiempo")
    print("2. Superficie Forestal Protegida promedio por continente")
    print("3. Superficie Forestal Protegida promedio por continente y periodo de tiempo")
    print("4. Comparacion Deforestacion con Superficie Forestal Protegida por periodos ")
    op = int(input("Ingresa una opcion: "))
    while op<0 or op>4:
        print("Opcion no disponible. Intentalo otra vez.")
        op = int(input("Ingresa una opcion: "))
    if op==1:
        sup.super_proteg_x_period(df)
    elif op==2:
         sup.super_prom_proteg_x_conti(df)
    elif op==3:
        sup.super_x_period_x_conti(df)        
    else:
        sup.Comparar_def_y_super_proteg(df)
        


def Deforestacion():
    data = pd.read_csv("data.csv",encoding = 'latin-1',delimiter=';',usecols=['Continente','Deforestacion','Periodos','Impulsores_deforestacion'])
    df=pd.DataFrame(data)
    print("Reportes a analizar: ")
    print("1. Deforestacion total por periodo de tiempo")
    print("2. Deforestacion total por continente y periodo de tiempo")
    print("3. Deforestacion por Impulsadores en America")
    print("4. Pais con mayor indice de deforestacion")
    op = int(input("Ingresa una opcion: "))
    while op<0 or op>4:
        print("Opcion no disponible. Intentalo otra vez.")
        op = int(input("Ingresa una opcion: "))
    if op==1:
        defo.Deforestacion_por_periodos_continentes(df)
    elif op==2:
        defo.grafico_barras_deforestacion(df)
    elif op==3:
        defo.impulsadores_america_defores(df)    
    else:
         defo.pais_mas_defo()



def Emisiones(df):
    print("Reportes a analizar: ")
    print("1. Emisiones de CO2 promedio por continente")
    print("2. Emisiones de CO2 promedio por periodo de tiempo")
    print("3. Emisiones de CO2 promedio por continente y periodo de tiempo")
    print("4. Emisiones de CO2 totales por continente (en %)")
    op = int(input("Ingresa una opcion: "))
    while op<0 or op>4:
        print("Opcion no disponible. Intentalo otra vez.")
        op = int(input("Ingresa una opcion: "))
    if op==1:
        emi.emision_prom_conti(df)
    elif op==2:
        emi.emision_x_period(df)
    elif op==3:
        emi.emi_cont_per(df)
    else:
         emi.porcen_emi(df)

def Impulsores(df):
    print("Reportes a analizar: ")
    print("1. Frecuencia Impulsores 2000-2020 ")
    print("2. Impulsor mas frecuente- Analisis  por continente")
    print("3. Media de los impulsores de la deforestacion por periodo")    
    op = int(input("Ingresa una opcion: "))
    while op<0 or op>4:
        print("Opcion no disponible. Intentalo otra vez.")
        op = int(input("Ingresa una opcion: "))
    if op==1:
        impul.Impulsadores_totales()
    elif op==2:
        impul.Impulsador_mas_repitente_x_continente()
    else:
        impul.Media_impulsadores(df)
  





