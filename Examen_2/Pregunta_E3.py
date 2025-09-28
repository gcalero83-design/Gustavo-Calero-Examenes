"""
Hazte Pro
ChatGPT


3.Crea un programa en Python que implemente una función llamada
convertir_precio(texto: str) -> float que (4 ptos):
1. Reciba un string que representa un precio en soles (ejemplo: "123.50",
"45", "20.99").
2. Intente convertirlo a un número decimal (float).
3. Tenga las siguientes excepciones:
o Si el texto está vacío, debe lanzar un ValueError("El precio no
puede estar vacío").
o Si el texto contiene caracteres inválidos (ejemplo: "abc",

"12a3"), debe lanzar un ValueError("Formato de precio inválido").
o Si el número es negativo, debe lanzar un ValueError("El precio no
puede ser negativo").
- El programa debe pedir tres precios al usuario, usar la función
convertir_precio y almacenarlos en una lista.
- Finalmente, mostrar:
o La lista con los precios convertidos.
o El precio promedio de los tres valores ingresados.

Ejemplo:
Entrada:
Ingrese precio 1: 100.69
Ingrese precio 2: -45
Ingrese precio 3: abc
Salida:
Error: el precio no puede ser negativo
Error: Formato de precio inválido
Precios válidos ingresados: [100.69]
Promedio: 100.5
"""
def convertir_precio(texto):
    if texto == "":
        raise ValueError("El precio no puede estar vacío")
    try:
        precio = float(texto)
    except:
        raise ValueError("Formato de precio inválido")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    return precio

precios = []
errores = []

for i in range(1, 4):
    entrada = input(f"Ingrese precio {i}: ")
    try:
        precio = convertir_precio(entrada)
        precios.append(precio)
    except ValueError as e:
        errores.append(str(e))

# Mostrar los errores
for error in errores:
    print("Error:", error)

# Mostrar los precios válidos
print("Precios válidos ingresados:", precios)

# Calcular y mostrar el promedio si hay precios válidos
if len(precios) > 0:
    promedio = sum(precios) / len(precios)
    print("Promedio:", promedio)
else:
    print("No hay precios válidos para calcular el promedio.")