"""
1. Crear una función llamada division_segura(a, b) que recibirá dos números e intentará devolver la división de a entre b
Si b es cero, debe capturar la excepción y mostrar mensaje “Error: no puedes dividir entre cero”
Si ambos valores son válidos deben imprimir el resultado Independientemente del resultado, debe imprimir “Operación finalizada” al final
- Usar try, except, finally
- Valida que los datos ingresados sean numéricos de lo contrario mostrar “Error: Entrada no numérica”
- Usarás la función al menos 3 veces incluyendo un caso de error
"""

try:
    a = int(input('Ingrese un numero:'))
    b = int(input('Ingrese un numero:'))
    fun=a/b
    print(fun)
except ValueError:
    print("¡Error: Debes introducir un número entero!")
except ZeroDivisionError:
    print("¡Error: No puedes dividir entre cero!")
finally:
    print('Operación finalizada!')