"""
8.Crear una clase Persona que contenga dos atributos: nombre y edad. Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo. Crearás un método
que indicará si debe pagar impuestos (que sería el 10% de su sueldo y si sueldo es superior a 4000 soles)
Instanciar la clase Empleado al menos para 3 empleados, mostrar el sueldo del empleado y cuánto debe pagar de impuesto.
"""
class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo: "))

    def pagar_impuestos(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
            print(f"El empleado {self.nombre} debe pagar {impuesto:.2f} soles de impuestos.")
        else:
            print(f"El empleado {self.nombre} no paga impuestos.")

empleado1 = Empleado()
empleado2 = Empleado()
empleado3 = Empleado()

print("\n--- Información de los empleados ---")
empleado1.pagar_impuestos()
empleado2.pagar_impuestos()
empleado3.pagar_impuestos()