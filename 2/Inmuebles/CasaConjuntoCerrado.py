from CasaUrbana import CasaUrbana

class CasaConjuntoCerrado(CasaUrbana):
    valorArea = 2500000  # atributo de clase

    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos, valorAdministración, tienePiscina, tieneCamposDeportivos):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos)
        self.valorAdministración = valorAdministración
        self.tienePiscina = tienePiscina
        self.tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        super().imprimir()
        print("Valor de la administración = " + str(self.valorAdministración))
        print("Tiene piscina? = " + str(self.tienePiscina))
        print("Tiene campos deportivos? = " + str(self.tieneCamposDeportivos))
        print()