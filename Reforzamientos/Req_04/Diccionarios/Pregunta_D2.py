"""
2.Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor del salario y DNI en consola.
También elimina el key edad de tu diccionario, incluyendo su valor. Mostrar finalmente el diccionario actualizado
"""
diccionario = {'Nombre': 'Gustavo','Edad': 42,'salario': 4500,'edad': 42}
lista=list(diccionario.values())
diccionario['DNI']=41836893
print(diccionario)
print(lista)
print(diccionario['salario'],diccionario['DNI'])
del diccionario['edad']
print(diccionario)