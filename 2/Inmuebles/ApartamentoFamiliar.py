from Apartamento import Apartamento

class ApartamentoFamiliar(Apartamento):
    valorArea = 2000000  # atributo de clase

    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, valorAdministración):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños)
        self.valorAdministración = valorAdministración

    def imprimir(self):
        super().imprimir()
        print("Valor de la administración = $" + str(self.valorAdministración))
        print()