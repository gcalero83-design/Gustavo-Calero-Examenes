import math

def cargar_entero_verificado():

    while True:
        entrada = input("Introduce un valor entero: ")
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Error: Debes ingresar solo números enteros.")

def mostrar_raiz_cuadrada(numero):

    if numero is not None and numero >= 0:
        raiz = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {raiz}")
    else:
        print("No se puede calcular la raíz cuadrada de un número negativo o inválido.")

def calcular_potencias(numero):

    if numero is not None:
        cuadrado = numero ** 2
        cubo = numero ** 3
        return {"cuadrado": cuadrado, "cubo": cubo}
    else:
        return None
