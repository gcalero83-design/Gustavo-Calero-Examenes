"""
1.Crear una clase Empleado que contenga los siguientes métodos,
uno que pida ingresar un nombre, apellido y edad, un método para
pedir su sueldo actual y otro método que lo imprima ambos resultados,
pero estarán contenidos en un diccionario. Comprobar los métodos
instanciado la clase respectivamente al menos para 3 empleados. Considerar en el constructor los valores necesarios.
"""
class Empleado:
    def __init__(self, nombre="", apellido="", edad=0):

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sueldo_actual = 0.0

    def ingresar_datos_personales(self):

        self.nombre = input("Ingrese el nombre del empleado: ")
        self.apellido = input("Ingrese el apellido del empleado: ")
        while True:
            try:
                self.edad = int(input("Ingrese la edad del empleado: "))
                if self.edad > 0:
                    break
                else:
                    print("La edad debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número válido para la edad.")

    def ingresar_sueldo_actual(self):

        while True:
            try:
                self.sueldo_actual = float(input("Ingrese el sueldo actual del empleado: "))
                if self.sueldo_actual >= 0:
                    break
                else:
                    print("El sueldo no puede ser negativo.")
            except ValueError:
                print("Por favor, ingrese un número válido para el sueldo.")

    def mostrar_datos_en_diccionario(self):

        datos = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Edad": self.edad,
            "Sueldo Actual": self.sueldo_actual
        }
        print("\n--- Datos del Empleado ---")
        print(datos)
        print("------------------------\n")

print("--- Creando Empleado 1 ---")
empleado1 = Empleado() # Se crea usando el constructor con valores por defecto
empleado1.ingresar_datos_personales()
empleado1.ingresar_sueldo_actual()
empleado1.mostrar_datos_en_diccionario()

print("--- Creando Empleado 2 ---")
empleado2 = Empleado("Ana", "López", 28) # Se crea usando el constructor con parámetros
empleado2.ingresar_sueldo_actual() # Solo necesita ingresar sueldo, ya tiene datos personales
empleado2.mostrar_datos_en_diccionario()

print("--- Creando Empleado 3 ---")
empleado3 = Empleado()
empleado3.ingresar_datos_personales()
empleado3.sueldo_actual = 3500.75 # Asignando sueldo directamente
empleado3.mostrar_datos_en_diccionario()