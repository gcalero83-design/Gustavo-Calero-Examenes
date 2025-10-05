"""
12. Escribe un programa que almacene información de un producto: Tu
nombre, nombre del producto, precio unitario (float), cantidad (int) e
imprimirá finalmente algo como lo siguiente:
Buen día Nombre, el detalle de su compra es el siguiente:
- Producto: Pollo a la brasa
- Precio unitario: 50.50
- Cantidad: 2
- Total a pagar: 101
"""
nombre=input("Ingresa tu nombre:")
producto=input("Ingresa tu producto:")
precio=input("Ingresa tu precio:")
cantidad=input("Ingresa tu cantidad:")
total= float(cantidad) * float(precio)
print("Buen día", nombre, "el detalle de su compra es el siguiente:")
print("- Producto:",producto)
print("- Precio:",precio)
print("- Cantidad:",cantidad)
print("- Total a pagar:",total)
