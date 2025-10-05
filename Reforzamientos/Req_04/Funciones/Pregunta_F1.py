"""
1.Pedir dos números positivos mediante terminal al usuario. Mostrar como salida el número cuya sumatoria de dígitos es el mayor
 y los números cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según sea conveniente.
"""
def suma_digitos(num):
    return sum(int(d) for d in str(num))

num_1 = int(input("Ingrese Primer número: "))
num_2 = int(input("Ingrese Segundo número: "))
sum1, sum2 = suma_digitos(num_1), suma_digitos(num_2)
print(num_1 if sum1 > sum2 else num_2, "tiene la mayor sumatoria de dígitos")
if sum1 < 10: print(num_1, "→ suma", sum1)
if sum2 < 10: print(num_2, "→ suma", sum2)

