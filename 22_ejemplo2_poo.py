""" Declarar una "Clase Auto" que contenga como atributos su marca, modelo y precio e instanciar dos objetos de 
esa clase. Ademas dicha clase contiene los metodos "Constructor" y "toString" por defecto """

class auto:
    def __init__(self, marca, modelo, precio) -> None:
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self) -> str:
        return f"Marca:{self.marca} Modelo:{self.modelo} Precio:{self.precio}"
    
auto1 = auto("Ford",2019,2.000000)
print (auto1)

auto2 = auto("Fiat",2009,1.500000)
print (auto2)