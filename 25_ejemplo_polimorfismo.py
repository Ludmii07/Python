class empleado:
    def __init__(self) -> None:
        self.nombre = input("Ingrese el nombre: ")
        self.sueldo = float (input("Ingrese su sueldo: "))

class jefe (empleado):
    def __init__(self) -> None:
        super().__init__()
        print("Paga impuestos")

class cajero (empleado):
    def __init__(self) -> None:
        super().__init__()
        print ("No  paga impuestos")

empleado1 = jefe ()
empleado1 = cajero ()