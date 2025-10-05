"""
2.Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la función una
vez y mostrar el resultado por consola). Los números serán ingresados y
solicitados al usuario.
"""
def mostrar_cuadrados(x, y):
    for i in range(x, y+1):
        print(i, "→", i**2)
num_ini = int(input("Ingresa Número inicial: "))
num_final = int(input("Ingresa Número final: "))
mostrar_cuadrados(num_ini, num_final)