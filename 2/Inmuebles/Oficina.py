from Local import Local

class Oficina(Local):
    valorArea = 3500000  # atributo de clase

    def __init__(self, identificadorInmobiliario, área, dirección, tipoLocal, esGobierno):
        super().__init__(identificadorInmobiliario, área, dirección, tipoLocal)
        self.esGobierno = esGobierno

    def imprimir(self):
        super().imprimir()
        print("Es oficina gubernamental = " + str(self.esGobierno))
        print()