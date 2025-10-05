"""
3.Pide al usuario que ingrese una frase y una palabra, obtén si la palabra está
dentro de la oración sin importar si está en mayúsculas o minúsculas.
En caso que aparezca, indica la posición del primer carácter en donde
empieza
Input: frase = “Python y sus enormes ventajas”, palabra = “Python”
Output: “Python aparece en la posición 0”
Métodos útiles: lower() y find()
"""

frase = input("Ingresa una frase: ")
palabra = input("Ingresa una palabra: ")

frase_lower = frase.lower()
palabra_lower = palabra.lower()

posicion = frase_lower.find(palabra_lower)

if posicion != -1:
    print(f'"{palabra}" aparece en la posición {posicion}')
else:
    print(f'"{palabra}" no se encontró en la frase')