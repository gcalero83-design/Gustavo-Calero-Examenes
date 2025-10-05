"""
Creando un archivo principal (main.py) donde importará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones:
-Una función que realizará la carga de un valor entero y que verifique que solamente tiene que ser numérico
-Una función que mostrará por pantalla la raíz cuadrada de dicho valor
-Y otra función que calculará el valor elevado al cuadrado y al cubo
de dicho número, puedes devolver un diccionario o una lista
-Utilizar el módulo math de python.
"""
import operaciones4

def main():
    numero = operaciones4.cargar_entero_verificado()
    operaciones4.mostrar_raiz_cuadrada(numero)
    potencias = operaciones4.calcular_potencias(numero)
    if potencias:
        print(f"Resultados de las potencias:")
        print(f"  - Cuadrado: {potencias['cuadrado']}")
        print(f"  - Cubo: {potencias['cubo']}")

if __name__ == "__main__":
    main()