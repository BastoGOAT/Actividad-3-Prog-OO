from Mascota import Mascota
class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto
    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

class GatoSinPelo(Gato):
    RAZAS = ['esfinge', 'elfo', 'donskoy']
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        if raza not in self.RAZAS:
            raise ValueError("Raza inválida para gato sin pelo")
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza 

class GatoPeloLargo(Gato):
    RAZAS = ['angora', 'himalayo', 'balinés', 'somalí']
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        if raza not in self.RAZAS:
            raise ValueError("Raza inválida para gato de pelo largo")
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

class GatoPeloCorto(Gato):
    RAZAS = ['azul ruso', 'británico', 'manx', 'devon rex']
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        if raza not in self.RAZAS:
            raise ValueError("Raza inválida para gato de pelo corto")
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

