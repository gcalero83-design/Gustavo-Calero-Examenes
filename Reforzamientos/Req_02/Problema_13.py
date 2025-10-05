"""
13. Crea un programa que convierta una temperatura en grados Celsius a
Fahrenheit. La fórmula que tiene que tener en cuenta es la siguiente:
F = (C * 9)/5 + 32
Deberá imprimir algo como lo siguiente:
La temperatura en °C: 30
Temperatura en Fahrenheit: 86.00
Realizarlo con dos distintos datos para la temperatura en Celsius (usar dos
variables iniciales para obtener dos temperaturas finales en Fahrenheit)
"""
Temp_Cel= input("Ingrese la temperatura en Celsius: ")
Temp_Fahr = (float(Temp_Cel) * 9)/5 + 32
print("La temperatura en °C:", Temp_Cel)
print("Temperatura en Fahrenheit:", Temp_Fahr)
