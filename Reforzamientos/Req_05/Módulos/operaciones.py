def cargar_numeros():
    print("Ingrese el primer número entero:")
    num1 = int(input())
    print("Ingrese el segundo número entero:")
    num2 = int(input())
    print("Ingrese el tercer número entero:")
    num3 = int(input())
    return num1, num2, num3

def obtener_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def encontrar_mayor(n1, n2, n3):
    return max(n1, n2, n3)