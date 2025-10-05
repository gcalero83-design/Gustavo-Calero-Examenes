"""
Creando un archivo principal (main.py) donde llamará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones:
-La primera función cargará a 3 números enteros que pedirá al usuario que ingrese por consola un valor.
-La segunda función solamente obtendrá la media de estos valores.
-La última función te indicará cuál es el mayor de los 3 números
-Desde el archivo principal importar al módulo y las funciones correspondiente usando las funciones anteriormente creadas en el módulo.
-Usarlo al menos para 3 casos distintos.
"""
import operaciones

print("--- Caso 1 ---")
numeros1 = operaciones.cargar_numeros()
n1_1, n1_2, n1_3 = numeros1
media1 = operaciones.obtener_media(n1_1, n1_2, n1_3)
print(f"La media de los números es: {media1}")

mayor1 = operaciones.encontrar_mayor(n1_1, n1_2, n1_3)
print(f"El número mayor es: {mayor1}\n")

print("--- Caso 2 ---")
numeros2 = operaciones.cargar_numeros()
n2_1, n2_2, n2_3 = numeros2
media2 = operaciones.obtener_media(n2_1, n2_2, n2_3)
print(f"La media de los números es: {media2}")
mayor2 = operaciones.encontrar_mayor(n2_1, n2_2, n2_3)
print(f"El número mayor es: {mayor2}\n")

print("--- Caso 3 ---")
numeros3 = operaciones.cargar_numeros()
n3_1, n3_2, n3_3 = numeros3
media3 = operaciones.obtener_media(n3_1, n3_2, n3_3)
print(f"La media de los números es: {media3}")
mayor3 = operaciones.encontrar_mayor(n3_1, n3_2, n3_3)
print(f"El número mayor es: {mayor3}\n")