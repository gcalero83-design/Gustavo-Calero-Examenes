"""
3. (2 ptos) Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente al usuario.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada exitosamente.
- La función que vas a crear va a capturar, la edad, nombre de un alumno, la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.
"""

from datetime import datetime


def conteo(func):
    def wrapper(*args, **kwargs):
        cantidad = len(args) + len(kwargs)
        print(f"Cantidad de parámetros usados: {cantidad}")

        if cantidad <= 1:
            print("Debe usar más de un parámetro para procesar la función.")
            return

        resultado = func(*args, **kwargs)

        print("La función fue ejecutada exitosamente.")
        return resultado

    return wrapper


@conteo
def registrar_alumno(nombre, edad, nota1, nota2, nota3, nota4):
    # Capturar la hora actual
    ahora = datetime.now()
    hora = ahora.hour
    minuto = ahora.minute

    print(f"{nombre} de {edad} años ha sido registrado a las"
          f" {hora} horas con {minuto} minutos.")

    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"La media del estudiante es: {promedio:.2f}")


print("---- Ejemplo 1 ----")
registrar_alumno("Pedro", 30, 15, 18, 17, 20)

print("\n---- Ejemplo 2 (caso con pocos parámetros) ----")


@conteo
def prueba_simple(x):
    print("Función simple ejecutada.")


prueba_simple(5)
