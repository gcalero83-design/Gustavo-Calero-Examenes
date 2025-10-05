"""
7.Realizar un programa donde se ingresarán por consola los nombres de los alumnos (indicar previamente la cantidad de alumnos a ingresar)
 de un curso y las notas de c/u. Guardarás la información en un diccionario donde las claves serán los nombres de c/u de estos alumnos y
 sus valores serán las notas de esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas.
"""
notas={}
print("Ingresar 5 Nombres con sus Notas")
nom_1=input("Ingresar nombre_1: ")
nota_1=input("Ingresar nota_1: ")
nom_2=input("Ingresar nombre_2: ")
nota_2=input("Ingresar nota_2: ")
nom_3=input("Ingresar nombre_3: ")
nota_3=input("Ingresar nota_3: ")
nom_4=input("Ingresar nombre_4: ")
nota_4=input("Ingresar nota_4: ")
nom_5=input("Ingresar nombre_5: ")
nota_5=input("Ingresar nota_5: ")
notas[nom_1]=int(nota_1)
notas[nom_2]=int(nota_2)
notas[nom_3]=int(nota_3)
notas[nom_4]=int(nota_4)
notas[nom_5]=int(nota_5)
print('Las notas registradas son:',notas)
print(nom_1,'tiene la nota de',nota_1)
print(nom_2,'tiene la nota de',nota_2)
print(nom_3,'tiene la nota de',nota_3)
print(nom_4,'tiene la nota de',nota_4)
print(nom_5,'tiene la nota de',nota_5)
valor=sum(notas.values())
conteo=len(notas)
print('Promedio de notas es:',valor/conteo)