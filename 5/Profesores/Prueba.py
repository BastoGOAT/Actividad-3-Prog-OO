from ProfesorTitular import ProfesorTitular
from Profesor import Profesor

class Prueba:
    @staticmethod
    def main():
        profesor1 = ProfesorTitular()
        profesor1._imprimir()
        profesor2 = Profesor()
        profesor2._imprimir()

if __name__ == "__main__":
    Prueba.main()