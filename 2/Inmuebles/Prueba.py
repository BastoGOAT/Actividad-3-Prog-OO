from ApartamentoFamiliar import ApartamentoFamiliar
from Apartaestudio import Apartaestudio

if __name__ == "__main__":
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    print("Datos apartamento")
    apto1.calcularPrecioVenta(apto1.valorArea)
    apto1.imprimir()

    print("Datos apartamento")
    aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1)
    aptestudio1.calcularPrecioVenta(aptestudio1.valorArea)
    aptestudio1.imprimir()