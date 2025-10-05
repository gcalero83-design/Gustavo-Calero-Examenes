"""
9.Una empresa desea gestionar las facturas pendientes que tiene por pagar, para esto se creará un diccionario donde tendrá por key el
número de factura “00054” y su value será el coste de la factura. El programa tendrá la opción de pedir nueva factura (por consola)
 que se agregará al diccionario. Cada vez que el área de contabilidad pague una factura se pedirá el número de factura que fue cancelada,
 si existe mostrar un mensaje donde indicará “La factura ya está cancelada” caso contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva factura se mostrará inmediatamente al diccionario actualizado.
"""
facturas = {}

while True:
    print("\n--- Lista facturas ---")
    print("1. Agregar nueva factura")
    print("2. Pagar una factura")
    print("3. Mostrar facturas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        numero = input("Ingrese número de factura: ")
        if numero in facturas:
            print("Esa factura ya existe.")
        else:
            costo = float(input("Ingrese el costo de la factura: "))
            facturas[numero] = costo
            print("Factura agregada correctamente.")
        print("Facturas actuales:", facturas)

    elif opcion == "2":
        numero = input("Ingrese número de factura a cancelar: ")
        if numero in facturas:
            del facturas[numero]
            print("La factura ya está cancelada.")
        else:
            print("El número de factura no existe.")
        print("Facturas actuales:", facturas)

    elif opcion == "3":
        print("Facturas registradas:", facturas)

    elif opcion == "4":
        print("Saliendo del sistema de facturas.")
        break

    else:
        print("Opción no válida, intente de nuevo.")