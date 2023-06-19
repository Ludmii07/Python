""" Codificar una funcion que reciba como parametro el nombre de una persona e imprima el saludo:
   Hola! Cómo estas NOMBRE?? cada vez que se invoque"""

def saludar (nombre):
    print (f"Hola! Cómo estas {nombre}??")

nombre = input ("Ingrese su nombre: ")
saludar (nombre)
nombre2 = input ("Ingrese su nombre otra vez: ")
saludar (nombre2)