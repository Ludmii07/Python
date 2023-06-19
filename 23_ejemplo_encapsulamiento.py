class Perro:
    __nombre = "Clea" # Atributos constantes 
    __raza = "Pitbull"
    __peso = 15.4 # Con los _ se encapsula, se privatiza y no se puede utilizar fuera de la clase

    def __ladrar(self):
        print("Guau! Guau!")
    
    def getNombre (self): # Para poder mostrar lo encapsulado
        return self.__nombre
    def getRaza (self):
        return self.__raza
    
    def getLadrar (self):
        return self.__ladrar()
    
perro1 = Perro()

print (perro1.getNombre())
print (perro1.getRaza())

perro1.getLadrar()