"""
Crear una función decoradora que dará los buenos días antes de ejecutar una función llamada saludo_inicial(nombre)
a ser decorada “Buenos días NOMBRE son las HORA horas con MINUTOS minutos” y luego de ser ejecutada lanzará un
mensaje diciendo “Hasta luego NOMBRE que tenga buen día”.
La función a decorar pedirá el nombre de una persona y retornará el mensaje.
Usar la función decorada al menos 3 veces
"""
import datetime

def decorador_saludo(func):
    def wrapper(nombre):

        ahora = datetime.datetime.now()
        hora_actual = ahora.strftime("%H")
        minuto_actual = ahora.strftime("%M")
        print(f"Buenos días {nombre} son las {hora_actual} horas con {minuto_actual} minutos.")

        resultado = func(nombre)

        print(f"Hasta luego {nombre} que tenga buen día.")
        return resultado
    return wrapper

@decorador_saludo
def saludo_inicial(nombre):
    mensaje = f"¡Hola, {nombre}! Un placer saludarte."
    print(mensaje)
    return mensaje

saludo_inicial("Ana")
saludo_inicial("Juan")
saludo_inicial("María")