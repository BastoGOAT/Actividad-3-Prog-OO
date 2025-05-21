from InmuebleVivienda import InmuebleVivienda

class Casa(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños, númeroPisos):
        super().__init__(identificadorInmobiliario, área, dirección, númeroHabitaciones, númeroBaños)
        self.númeroPisos = númeroPisos

    def imprimir(self):
        super().imprimir()
        print("Número de pisos = " + str(self.númeroPisos))
        