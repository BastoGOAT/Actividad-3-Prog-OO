from Local import Local

class LocalComercial(Local):
    valorArea = 3000000  # atributo de clase

    def __init__(self, identificadorInmobiliario, área, dirección, tipoLocal, centroComercial):
        super().__init__(identificadorInmobiliario, área, dirección, tipoLocal)
        self.centroComercial = centroComercial

    def imprimir(self):
        super().imprimir()
        print("Centro comercial = " + self.centroComercial)
        print()