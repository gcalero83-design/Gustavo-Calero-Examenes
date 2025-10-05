"""
Intervención
Usando propiedades de string
Requisitos:
- Ingresar su nombre y apellido por consola
(variables distintas)
- Obtener el tamaño de tu nombre completo y muéstralo en consola
- Imprimir el resultado final, todo en mayúsculas: .upper()
- Indicar mediante condicionales si el tamaño del nombre es mayor o no al apellido ingresado
- Solamente ingresar el apellido paterno
"""
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido paterno: ")
nombre_completo = nombre + " " + apellido
print("Tamaño nombre completo:", len(nombre_completo))
print("En mayúsculas:", nombre_completo.upper())
if len(nombre) > len(apellido):
    print("El nombre es más largo que el apellido")
elif len(nombre) < len(apellido):
    print("El apellido es más largo que el nombre")
else:
    print("El nombre y apellido tienen el mismo tamaño")