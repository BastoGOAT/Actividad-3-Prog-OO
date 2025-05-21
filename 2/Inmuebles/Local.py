from Inmueble import Inmueble
from enum import Enum

class Tipo(Enum):
    INTERNO = 1
    CALLE = 2

class Local(Inmueble):
    def __init__(self, identificadorInmobiliario, área, dirección, tipoLocal):
        super().__init__(identificadorInmobiliario, área, dirección)
        self.tipoLocal = tipoLocal

    def imprimir(self):
        super().imprimir()
        print("Tipo de local = " + self.tipoLocal.name)