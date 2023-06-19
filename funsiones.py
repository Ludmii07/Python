def sumar (numero1,numero2):
    suma = numero1 + numero2
    return suma

def restar (numero1,numero2): 
    resta = numero1 - numero2
    return resta

def multiplicar (numero1,numero2): 
    producto = numero1 * numero2
    return producto

def dividir (numero1,numero2):
    if numero2 != 0:
        cociente = numero1 / numero2
    else:
        cociente = "Division por cero"
    return cociente 
