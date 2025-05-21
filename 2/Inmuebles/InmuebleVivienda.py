from Inmueble import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños):
        super().__init__(identificadorInmobiliario, área, dirección)
        self.númeroHabitaciones = númeroHabitaciones
        self.númeroBaños = númeroBaños

    def imprimir(self):
        super().imprimir()
        print("Número de habitaciones = " + str(self.númeroHabitaciones))
        print("Número de baños = " + str(self.númeroBaños))
        