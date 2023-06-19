precio = int (input ("Ingrese el precio:"))

valor_iva = int (input ("Igrese el porcentaje del I.V.A.:"))

IVA = precio + (precio * valor_iva /100)

print ("Precio final:", IVA)