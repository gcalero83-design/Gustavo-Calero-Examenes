"""
4.Crear una función saluda_fecha(nombre, dia, mes, anio) que contendrá una
excepción para el siguiente bloque de código y tu programa no se bloquee.
Además, imprime un mensaje al usuario la causa y/o solución (Pedir
nombre, día, mes, año por consola):
Nombre: No debe recibir un dato numérico, sino decírselo al usuario Día, mes
y año: No debe recibir un dato string, sino decírselo al usuario

cadena = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
# Hello Leonardo, hoy estamos 04 de agosto del 2025

Independientemente del resultado, debe imprimir “Operación
finalizada” al final
- Usar try, except, finally
Usar la función al menos 3 veces, incluyendo casos de error.
"""
def saluda_fecha(nombre, dia, mes, año):
    try:

        if nombre.isdigit():
            raise ValueError("El nombre no debe ser numérico. Ingresa un nombre válido.")

        dia = int(dia)
        mes = int(mes)
        año = int(año)

        meses = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}

        if mes not in meses:
            raise ValueError("El mes ingresado no es válido (debe estar entre 1 y 12).")

        cadena = f"Hello {nombre}, hoy estamos {dia:02d} de {meses[mes]} del {año}"
        print(cadena)

    except ValueError as e:
        print("Error:", e)

    finally:
        print("Operación finalizada\n")

print("Caso 1: válido")
saluda_fecha("Leonardo", 4, 8, 2025)

print("Caso 2: nombre numérico")
saluda_fecha("2684", 4, 8, 2025)

print("Caso 3: mes inválido")
saluda_fecha("Juan", 5, 20, 2015)

print("Caso 4: entrada no numérica en día")
saluda_fecha("Juan", "cuatro", 8, 2023)
