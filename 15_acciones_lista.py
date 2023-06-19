nombres = ["Alan","Denise","Belen","Carlos"]
print (nombres) # Imprime todos los nombres
print (nombres[2]) # Para elegir que objeto imprimir
print (nombres[-1]) # Muestra el ultimo elemento de la lista

nombres.append ("Gustavo") # Para agregar elementos (se agregan al final de la lista)
print (nombres)

nombres.pop (3) # Elimina el objeto indicado, si no se indica ninguno se elimina el ultimo objeto de la lista
print (nombres)

nombres.sort () # Ordena la lista
print (nombres)

nombres.sort (reverse=1) # Ordena la lista al reves
print (nombres)