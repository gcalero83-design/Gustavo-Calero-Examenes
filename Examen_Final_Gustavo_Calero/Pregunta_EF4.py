"""
4. (2 ptos) Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con m minutos y S segundos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**kwards) para usar más de 6 valores en la función (value_7 = 10,
value_8 = 22, value_9=45) y visualizar los resultados usando el decorador
implementado con un mínimo tres ejemplos.
"""

from datetime import datetime


def mostrar_hora_y_sumar(func):
    def wrapper(*args, **kwargs):

        ahora = datetime.now()
        print(f"El decorador está siendo ejecutado a las"
              f" {ahora.hour} con {ahora.minute}"
              f" minutos y {ahora.second} segundos")

        suma_args = sum(args)
        suma_kwargs = sum(kwargs.values())
        suma_total = suma_args + suma_kwargs
        print(f"La suma de todos los valores es: {suma_total}")

        return func(*args, **kwargs)
    return wrapper


@mostrar_hora_y_sumar
def mayor_valor(*args, **kwargs):
    valores = list(args) + list(kwargs.values())
    mayor = max(valores)
    print(f"El mayor valor ingresado es: {mayor}\n")


print("---- Ejemplo 1 ----")
mayor_valor(10, 20, 5, 7, 8, 12)

print("---- Ejemplo 2 ----")
mayor_valor(4, 15, 9, value_7=10, value_8=22, value_9=45)

print("---- Ejemplo 3 ----")
mayor_valor(100, 200, 150, 90, value_7=300, value_8=50)
