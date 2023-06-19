# Crear una lista de 5 números al azar entre 0 y 9, que esten ordenados y no se repitan

import random 

lista = []
número = random.randint (0,9) # Genera un número al azar
while len(lista) < 5:
    if número not in lista:
        lista.append(número)
    número = random.randint (0,9)
lista.sort ()
print (lista)
    