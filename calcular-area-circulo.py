#Paso 1: Solicitar al usuario que ingrese el radio del circulo.

import math

radio = float(input("Por favor, ingrese el radio del circulo: "))
 
#Paso 2: Calcular el area del circulo con la formula area = π * radio^2

area = math.pi * (radio**2)

    
#Paso 3: Mostrar al usuario rsultado del area
print("El area del circulo con radio" , radio, "es:" , area)

