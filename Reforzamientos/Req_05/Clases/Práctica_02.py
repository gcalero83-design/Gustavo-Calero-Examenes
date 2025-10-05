"""
2.Crear una clase llamada Circulo que contenga radio en su constructor y que contenga un método área que devuelva el área de un círculo.
Adicionalmente habrá un método que devuelva el perímetro del círculo. También habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
class Circulo:
    def __init__(self, radio):
         self.radio = radio
    def area_circulo(self):
        return math.pi * (self.radio ** 2)

    def perimetro_circulo(self):
        return 2 * math.pi * self.radio

    def pedir_radio(self):
        while True:
            try:
                radio_ingresado = float(int(input("Ingrese Radio: ")))
                if radio_ingresado >= 0:
                    self.radio = radio_ingresado
                    break
                else:
                    print("Radio invalido")
            except ValueError:
                print("Radio invalido")

circulo1 = Circulo(5)
circulo2 = Circulo(0)
print(f"## Resultados del Círculo 1")
print(f"El radio del Círculo 1 es: ", format(f"{circulo1.radio:.2f}"))
print(f"El área del Círculo 1 es: ", circulo1.area_circulo())
print(f"El perímetro del Círculo 1 es: ", circulo1.perimetro_circulo())

# Pedir radio para el segundo círculo y mostrar resultados
print(f"\n## Resultados del Círculo 2")
circulo2.pedir_radio()
print(f"El radio del Círculo 2 es: ",format(f"{circulo2.radio:.2f}"))#format(f"{Volumen:.2f}"
print(f"El área del Círculo 2 es: ", circulo2.area_circulo())
print(f"El perímetro del Círculo 2 es: ", circulo2.perimetro_circulo())



