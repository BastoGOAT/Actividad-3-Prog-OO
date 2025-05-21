from Casa import Casa

class CasaRural(Casa):
    valorArea = 1500000  # atributo de clase

    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos, distanciaCabera, altitud):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos)
        self.distanciaCabera = distanciaCabera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print("Distancia la cabecera municipal = " + str(self.distanciaCabera) + " km.")
        print("Altitud sobre el nivel del mar = " + str(self.altitud) + " metros.")
        print()