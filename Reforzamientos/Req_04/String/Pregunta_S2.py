"""
2.Crear un programa que cuente cuántas veces aparece cada vocal en la
oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()
"""

cadena = "Programación en Python"

cadena = cadena.lower()

vocales = "aeiou"

for v in vocales:
    print(f"{v}: {cadena.count(v)}")
