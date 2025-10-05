"""
2.Crear una función y dentro la respectiva excepción o excepciones para el
siguiente bloque de código para que tu programa no se bloquee, ya que solo
aceptará datos tipos entero y además imprimir un mensaje al usuario la causa
y/o solución. También debe indicar el índice donde ingresarás este nuevo dato,
si el índice está fuera de rango indicárselo al usuario:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]: No es posible ingresar el dato, índice fuera de rango
- Usarás dos tipos diferentes de excepciones (IndexError TypeError) y
- Usarás la función al menos 3 veces incluyendo un caso de error.
"""

lista = [2, 6, 10, 4, 5, 23, 1]

def insertar_lista(valor, indice):
    try:
        valor = int(valor)
        lista[indice] = valor
        print("Lista actualizada:", lista)
    except ValueError:
        print("Error: el valor debe ser entero")
    except IndexError:
        print("Error: índice fuera de rango")
    except TypeError:
        print("Error: índice debe ser un número entero")

print("Caso 1: válido")
insertar_lista(99, 2)

print("\nCaso 2: índice fuera de rango")
insertar_lista(77, 10)

print("\nCaso 3: índice con tipo incorrecto")
insertar_lista(55, "tres")
