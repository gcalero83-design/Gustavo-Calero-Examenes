"""
1.Dada una frase u oración encontrar que palabra es la que tiene más
caracteres y cuántos caracteres tiene
Input: “La programación en Python es poderosa”
Output: “programación” – 12 caracteres
"""

cadena = "La programación en Python es poderosa"

palabras = cadena.split()

palabra_larga = max(palabras, key=len)

cantidad = len(palabra_larga)

print(f'"{palabra_larga}" - {cantidad} caracteres')