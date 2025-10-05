"""Manejo de errores
Requisitos:
- Crear una función la cuál va a evaluar una lista y un índice
- Habrá una exepción donde dentro de la función que sa a considerar 
una lista con 4 valores
- Cuando se va a modificar una de las posiciones no existentes
crear un nuevo índice y darle un valor de 0
- Mostrar la lista final
"""
def evaluar_lista(lista, indice, valor):
    try:
        lista[indice] = valor
    except IndexError:
        print("Índice fuera de rango, se agregará un nuevo valor = 0")
        lista.append(0)
    finally:
        print("Lista final:", lista)

mi_lista = [21, 24, 5, 99]

evaluar_lista(mi_lista, 4, 125)

evaluar_lista(mi_lista, 25, 300)
