# Realizar un programa de Python que permita ingresar el valor de una compra relizada por una persona.
# En el caso de ser un importe mayor a $10.000 informe que debe registrarse su D.N.I.
importe = float (input ("Ingrese el importe a evaluar:"))

if importe > 10000:
    print ("Debe registrar su DNI")

print ("Gracias por su compra!")