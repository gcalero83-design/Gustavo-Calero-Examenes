"""
6. Calcular la media de 5 datos (floats), cada dato debe estar en una variable
y la media también. Mostrar el resultado en pantalla y el tipo de dato
también mostrarlo.
"""
from numpy import average

var_1=float(3.14159)
var_2=float(5.5)
var_3=float(4.5)
var_4=float(29)
var_5=float(562)
resultado= average([var_1,var_2,var_3,var_4,var_5])
print(resultado)
print(type(resultado))
