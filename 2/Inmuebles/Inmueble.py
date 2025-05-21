class Inmueble:
    def __init__(self, identificadorInmobiliario, área, dirección):
        self.identificadorInmobiliario = identificadorInmobiliario
        self.área = área
        self.dirección = dirección
        self.precioVenta = 0.0

    def calcularPrecioVenta(self, valorArea):
        self.precioVenta = self.área * valorArea
        return self.precioVenta

    def imprimir(self):
        print("Identificador inmobiliario = " + str(self.identificadorInmobiliario))
        print("Area = " + str(self.área))
        print("Dirección = " + self.dirección)
        print("Precio de venta = $" + str(self.precioVenta))
        