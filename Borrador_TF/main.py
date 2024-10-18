import Fx as GD
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('data.csv',delimiter=';',encoding='latin-1')
data=pd.DataFrame(df)
df=data.set_index('Pais')

GD.welcome()
nombre= GD.pide_nombre()
print("Hola ", nombre, ", bienvenido a GreenData!")
print()
edad = GD.pide_anio()
print()
sexo = GD.genero()
print()
pais = GD.pais_pro()



print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print()
GD.ver_perfil(nombre, edad, sexo, pais)
print("--------------------------------------------------")
opcion = 1
while opcion != 0:
    opcion = GD.menu()
    print()
    if opcion == 1:
        GD.objetivos()      
    elif opcion == 2:
        GD.ver_perfil(nombre, edad, sexo, pais) 
        print()
    elif opcion == 3:
        nombre = GD.pide_nombre()
        edad = GD.pide_anio()      
        sexo = GD.genero()
        pais = GD.pais_pro()        
        GD.ver_perfil(nombre, edad, sexo, pais)
    elif opcion == 4:
         GD.tabla_general(df)      
    elif opcion == 5:
         GD.Expansion_Forestal(data,df)         
    elif opcion == 6:
         GD.Deforestacion()     
    elif opcion == 7:
        GD.Emisiones(df)
    elif opcion == 8:
        GD.Impulsores(df)
    elif opcion == 9:
        GD.Superficie_Protegida(df)      
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar GreenData. Hasta la vista!")
