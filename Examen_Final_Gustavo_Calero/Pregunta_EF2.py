"""
2. Utilizar el concepto de módulo necesariamente. Y escribir un programa para el
manejo de listas el cuál cumplirá los siguientes requerimientos (2 ptos):
Reglas:
- Crear una función que le permitirá almacenar X números aleatorios en
una lista y finalmente los imprimirá por consola al llamar la función. X
solo puede ser entero. No otro tipo de dato. Y también un índice
existente en la lista (usar para esto excepciones)
- Crear una función que le permita almacenar los números no repetidos de
la lista anterior, la función retornará este valor para que pueda ser
impreso por consola.
- Crear una función donde se creará una lista para ordenar de mayor a
menor la lista que se creó en el ítem anterior (número no repetidos) y
otra lista para ordenarlas de menor a mayor, retornar este valor e
imprimirlos por consola.
- Crear una función para indicar cuál es el mayor número par de la lista
(lista de la regla 2), retornar este valor e imprimirlo por consola.
- Crear el archivo main.py, donde solo llamarás las anteriores funciones que
se encontrarán alojadas en un módulo (probarlo para dos casos mínimo)
"""

import random


def crear_lista_aleatoria(x, indice):
    try:
        if not isinstance(x, int):
            raise TypeError("X debe ser un número entero.")
        lista = [random.randint(1, 100) for _ in range(x)]
        print(f"Lista generada: {lista}")

        print(f"Elemento en el índice {indice}: {lista[indice]}")
        return lista
    except TypeError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Error: El índice no existe en la lista.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def lista_sin_repetidos(lista):
    nueva_lista = list(set(lista))
    print(f"Lista sin repetidos: {nueva_lista}")
    return nueva_lista


def ordenar_lista(lista):
    lista_mayor_a_menor = sorted(lista, reverse=True)
    lista_menor_a_mayor = sorted(lista)
    print(f"Orden de mayor a menor: {lista_mayor_a_menor}")
    print(f"Orden de menor a mayor: {lista_menor_a_mayor}")
    return lista_mayor_a_menor, lista_menor_a_mayor


def mayor_par(lista):
    pares = [num for num in lista if num % 2 == 0]
    if pares:
        mayor = max(pares)
        print(f"El mayor número par es: {mayor}")
        return mayor
    else:
        print("No hay números pares en la lista.")
        return None
