"""
8.Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”
"""
agenda={}
print("Ingresar Nombres y Número de Celular")
nom_1=input("Ingresar nombre_1: ")
cel_1=input("Ingresar Num. Celular_1: ")
nom_2=input("Ingresar nombre_2: ")
cel_2=input("Ingresar Num. Celular_2: ")
agenda[nom_1]=cel_1
agenda[nom_2]=cel_2
print(agenda)
busqueda=input("Ingresar nombre: ")
print(agenda.get(busqueda,'No se encuentra el registro'))