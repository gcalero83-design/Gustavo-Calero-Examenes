# operaciones.py
import random

def generar_numeros_aleatorios():

  numeros = [random.randint(0, 100) for _ in range(30)]
  print("Lista de números aleatorios generada:", numeros)
  return numeros

def ordenar_y_mostrar_lista(lista):

  lista_ordenada = sorted(lista)
  print("Lista ordenada:", lista_ordenada)
  return lista_ordenada

def encontrar_mayor_numero(lista):

  if not lista:
    print("La lista está vacía.")
    return None
  mayor = max(lista)
  print("El mayor número de la lista es:", mayor)
  return mayor