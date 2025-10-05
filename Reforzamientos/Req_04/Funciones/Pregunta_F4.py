"""
4.Pedir al usuario que ingrese un nombre y apellidos el cual será usada
por un parámetro para una función que se creará e indicará cuantas letras
tiene el nombre solamente. Usar la función un mínimo de dos veces para dos
personas e indicar quien tiene el nombre con mayor número de caracteres
(condicional)
"""
def contar_letras(nombre):
    return len(nombre)
nom_1 = input("Ingresa nombre y apellido de la primera persona: ")
nom_2 = input("Ingresa nombre y apellido de la segunda persona: ")
nombre1 = nom_1.split()[0]
nombre2 = nom_2.split()[0]
num_letras1 = contar_letras(nombre1)
num_letras2 = contar_letras(nombre2)
print(f"{nombre1} tiene {num_letras1} letras")
print(f"{nombre2} tiene {num_letras2} letras")
if num_letras1 > num_letras2:
    print(f"{nombre1} tiene más letras")
elif num_letras2 > num_letras1:
    print(f"{nombre2} tiene más letras")
else:
    print("Ambos nombres tienen la misma cantidad de letras")