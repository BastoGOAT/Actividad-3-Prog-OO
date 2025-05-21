from CasaUrbana import CasaUrbana

class CasaIndependiente(CasaUrbana):
    valorArea = 3000000  # atributo de clase

    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos)

    def imprimir(self):
        super().imprimir()
        print()