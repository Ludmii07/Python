"""Crear un programa para realizar un sorteo y elegir un nombre al azar"""

import random 

nombres = []
while True:
    nombre = input ("Ingrese un nombre o un '0' para terminar: ")
    
    if nombre != "0":
        nombres.append (nombre)
    else:
        break

print (nombres)

nombre_al_azar = random.choice(nombres)
print ("El ganador/a del premio es: ", nombre_al_azar)