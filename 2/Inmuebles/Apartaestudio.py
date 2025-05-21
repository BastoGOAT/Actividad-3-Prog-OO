from Apartamento import Apartamento

class Apartaestudio(Apartamento):
    valorArea = 1500000  # atributo de clase

    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños):
        # En el constructor Java, siempre se pasan 1 y 1 para habitaciones y baños
        super().__init__(identificadorInmobiliario, área, dirección, 1, 1)

    def imprimir(self):
        super().imprimir()
        print()