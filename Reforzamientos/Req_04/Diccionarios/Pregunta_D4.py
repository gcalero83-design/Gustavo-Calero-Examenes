""""
4.Crear un diccionario con 6 departamentos del país.
-
Borrar cualquier departamento, usando la palabra reservada del.
-
Actualizar el penúltimo departamento por otro.
-
Comprobar que no existe este departamento borrado dentro del diccionario.\
"""
departamentos={'A':'Lima','B':'Piura','C':'Arequipa','D':'Cajamarca','E':'La Libertad','F':'Junin'}
print(departamentos)
lista1=list(departamentos.keys())
del depa['C']
clave = lista1[-2]
print(clave)
departamentos[clave]='Ica'
print(departamentos)