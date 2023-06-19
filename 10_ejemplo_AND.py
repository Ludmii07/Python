""" 
PRESTAMO DE UN BANCO: 
 Desarrollar un programa en python que verifique la edad de una persona e indique si es posible otorgarle
un prestamo personal 
 Las condiciones de otorgamiento son: 
 A) Se a mayor de edad 
 B) Sea menor de 65 años
En caso contrario no sera posible otorgarle el credito.

""" 

edad = int (input ("Ingrese la edad de la persona:"))
if edad >= 18 and edad < 65:
    print ("¡Felicitaciones! Se le ha otorgado el crédito.")
else:
    print ("No es posible dar el préstamo por el momento:")