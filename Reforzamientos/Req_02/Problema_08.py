"""
8.Usando la condicional if imprimir por pantalla si una lista ([]) está vacía o
no, comprobar con una lista vacía y otra con una lista con dato al menos
([dato_1, dato_2]).
"""
from numpy.ma.core import count

lista_1 = []
lista_2 = [1, 2, 3]
if len(lista_1) <=0:
    print("Lista 1 vacía")
if len(lista_2) >=0:
    print("Lista 2 tiene", len(lista_2), "elementos")
