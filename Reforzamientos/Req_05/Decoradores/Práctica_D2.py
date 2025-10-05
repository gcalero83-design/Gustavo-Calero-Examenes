"""
2.Haciendo el uso de *args y **kwargs aplicarlo debidamente para decorar una función que
recibirá 6 argumentos los cuales se multiplicarán entre ellos (3 de ellos serán usado con **kwargs) Mensaje previo al usar el decorador “Está por ejecutarse la función” y mensaje luego de usar el decorador “La función ha sido ejecutado correctamente”
Usar la función decorada al menos 3 veces
"""
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")

        multiplicador_args = 1
        if args:

            multiplicador_args = args[0] * args[1] * args[2]

        multiplicador_kwargs = 1
        if kwargs:

            for valor in kwargs.values():
                multiplicador_kwargs *= valor

        resultado_final = multiplicador_args * multiplicador_kwargs

        print(f"Resultado final calculado: {resultado_final}")  # Mostrar el resultado intermedio para claridad
        resultado_funcion = func(*args, **kwargs)
        print("La función ha sido ejecutado correctamente")
        return resultado_funcion

    return wrapper


@mi_decorador
def multiplicar_argumentos_con_decorador(a, b, c, d, e, f):

    print(f"Argumentos posicionales: a={a}, b={b}, c={c}")
    print(f"Argumentos de palabra clave: {d}, {e}, {f}")
    return a * b * c * d * e * f

print("--- Primera llamada ---")
multiplicar_argumentos_con_decorador(2, 3, 4, 5, 6, 7)  # Los primeros 3 van a los args, los otros a los kwargs
print("\n--- Segunda llamada ---")
multiplicar_argumentos_con_decorador(1, 2, 3, 8, 9, 10)
print("\n--- Tercera llamada ---")
multiplicar_argumentos_con_decorador(10, 20, 30, 1, 1, 1)