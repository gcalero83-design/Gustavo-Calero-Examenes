"""
Creando un archivo principal (main.py) donde importará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones:
-Una función que genere 30 números enteros aleatorios entre 0 y 100, y muestre en pantalla esta lista de números aleatorios
-Otra función que ordene los valores de una lista y volver a mostrarla en pantalla
-Otra función que me indicará cuál es el mayor de todos estos números de la lista
"""
import operaciones3
lista_de_numeros = operaciones3.generar_numeros_aleatorios()
lista_ordenada = operaciones3.ordenar_y_mostrar_lista(lista_de_numeros)
operaciones3.encontrar_mayor_numero(lista_de_numeros)