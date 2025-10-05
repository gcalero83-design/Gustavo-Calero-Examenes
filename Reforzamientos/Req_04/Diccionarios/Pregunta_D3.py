"""
3.Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tienes.
"""
diccionario = {'Nombre': 'Gustavo','Edad': 42,'salario': 4500,'edad': 42}
lista=list(diccionario.values())
diccionario['DNI']=41836893
print(diccionario)
print(lista)