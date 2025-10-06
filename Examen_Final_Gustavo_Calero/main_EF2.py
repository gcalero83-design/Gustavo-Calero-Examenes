import Pregunta_EF2 as ol

print("===== 🧪 PRUEBA 1 =====")
lista = ol.crear_lista_aleatoria(10, 3)
lista_unica = ol.lista_sin_repetidos(lista)
ol.ordenar_lista(lista_unica)
ol.mayor_par(lista_unica)

print("\n===== 🧪 PRUEBA 2 =====")
lista2 = ol.crear_lista_aleatoria(8, 5)
lista_unica2 = ol.lista_sin_repetidos(lista2)
ol.ordenar_lista(lista_unica2)
ol.mayor_par(lista_unica2)
