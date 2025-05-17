#1. Ejercicio 4.1 página 194
class Cuenta:
    saldo = float
    numeroConsignaciones = int(0)
    numeroRetiros = int(0)
    tasaAnual = float
    comisionMensual = float(0)
    def __init__(self, saldo: float, tasaAnual: float):
        self.saldo = saldo
        self.tasaAnual = tasaAnual
        self.numeroConsignaciones = 0
        self.numeroRetiros = 0
        self.comisionMensual = 0.0

    def consignar(self, cantidad=float):
        self.saldo += cantidad
        self.numeroConsignaciones += 1

    def retirar(self, cantidad=float):
        nuevoSaldo = self.saldo - cantidad
        if nuevoSaldo >= 0:
            self.saldo -= cantidad
            self.numeroRetiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual")

    def calcularInteres(self):
        tasaMensual = self.tasaAnual / 12
        interesMensual = self.saldo * tasaMensual
        self.saldo += interesMensual

    def extractoMensual(self):
        self.saldo -= self.comisionMensual
        self.calcularInteres()

class CuentaAhorros(Cuenta):
    activa = bool
    def __init__(self, saldo: float, tasa: float):
        super().__init__(saldo, tasa)
        if saldo < 10000:
            self.activa = False
        else:
            self.activa = True

    def retirar(self, cantidad: float):
        if self.activa:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self.activa:
            super().consignar(cantidad)

    def extractoMensual(self):
        if self.numeroRetiros > 4:
            self.comisionMensual += (self.numeroRetiros - 4) * 1000
        super().extractoMensual()
        if self.saldo < 10000:
            self.activa = False

    def imprimir(self):
        print("Saldo = $", self.saldo)
        print("Comision mensual = $", self.comisionMensual)
        print("Número de transacciones = ", (self.numeroConsignaciones + self.numeroRetiros))
        print("------------------------")

class CuentaCorriente(Cuenta):
    sobregiro = float
    def __init__(self, saldo: float, tasa: float):
        super().__init__(saldo, tasa)
        self.sobregiro = 0.0

    def retirar(self, cantidad: float):
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro -= resultado
            self.saldo = 0
            self.numeroRetiros += 1
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self.sobregiro > 0:
            residuo = self.sobregiro - cantidad
            if residuo > 0:
                self.sobregiro = residuo
                self.saldo = 0
            else:
                self.sobregiro = 0
                self.saldo = -residuo
        else:
            super().consignar(cantidad)

    def extractoMensual(self):
        super().extractoMensual()

    def imprimir(self):
        print("Saldo = $", self.saldo)
        print("Cargo mensual = $", self.comisionMensual)
        print("Número de transacciones = ", self.numeroConsignaciones + self.numeroRetiros)
        print("Valor de sobregiro = $", self.sobregiro)
        print("----------------------------------")

if __name__ == "__main__":
    print("Cuenta de Ahorros")
    saldoInicialAhorros = float(input("Ingrese saldo inicial: $"))
    tasaAhorros = float(input("Ingrese tasa de interés = "))
    cuenta1 = CuentaAhorros(saldoInicialAhorros, tasaAhorros)
    cantidadDepositar = float(input("Ingresar cantidad a Consignar: $"))
    cuenta1.consignar(cantidadDepositar)
    cantidadRetirar = float(input("Ingresar cantidad a Retirar: $"))
    cuenta1.retirar(cantidadRetirar)
    cuenta1.extractoMensual()
    cuenta1.imprimir()