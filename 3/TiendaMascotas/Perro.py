from Mascota import Mascota
class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde
    @staticmethod
    def sonido():
        print("Los perros ladran")

class PerroPequeño(Perro):
    RAZAS = ['caniche', 'yorkshire terrier', 'schnauzer', 'chihuahua']
    def __init__(self, nombre, edad, color, peso, muerde, raza):
        if raza not in self.RAZAS:
            raise ValueError("Raza inválida para perro pequeño")
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

class PerroMediano(Perro):
    RAZAS = ['collie', 'dálmata', 'bulldog', 'galgo', 'sabueso']
    def __init__(self, nombre, edad, color, peso, muerde, raza):
        if raza not in self.RAZAS:
            raise ValueError("Raza inválida para perro mediano")
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

class PerroGrande(Perro):
    RAZAS = ['pastor alemán', 'doberman', 'rotweiller']
    def __init__(self, nombre, edad, color, peso, muerde, raza):
        if raza not in self.RAZAS:
            raise ValueError("Raza inválida para perro grande")
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza