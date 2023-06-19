""" Crear una "Clase Persona" que contenga los atributos de Nombre y Edad, y una "Sub Clase Alumno"
que herede los atributos y metodos de la clase persona y contenga como atributo propio el "Curso" donde
estudia. """

class persona:
    def __init__(self) -> None:
        self.nombre = input ("Ingrese el nombre: ")
        self.edad = int (input ("Ingrese la edad: "))

    def __str__(self) -> str:
        return f"Nombre:{self.nombre} Edad:{self.edad}"
    
class alumno (persona):
    def __init__(self) -> None:
        super().__init__()
        self.curso = input ("Ingrese el curso del alumno: ")
    
    def __str__(self) -> str:
        return super().__str__() + f" Cursa en: {self.curso}"

    
alumno1 = alumno()
print (alumno1)
