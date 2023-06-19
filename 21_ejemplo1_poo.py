class persona:
    def __init__(self,nombre, edad, peso) -> None:
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def __str__(self) -> str:
        return f"Nombre:{self.nombre} Edad:{self.edad} Peso:{self.peso}"

persona1 = persona ("Juan", 25, 70.4)
persona2 = persona ("Maria", 18, 60.2)

print (persona1)
print (persona2)