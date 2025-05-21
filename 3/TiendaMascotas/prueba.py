#Probando el Código
from Gatos import GatoSinPelo, GatoPeloLargo, GatoPeloCorto, Gato
from Perro import PerroPequeño, PerroMediano, PerroGrande, Perro

if __name__ == "__main__":
    print("---- PRUEBA DE GATOS ----")
    gato1 = GatoSinPelo("Tralalero", 2, "gris", 1.2, 2.5, "esfinge")
    print(f"GatoSinPelo: nombre={gato1.nombre}, raza={gato1.raza}, color={gato1.color}, altura de salto={gato1.altura_salto}, longitud de salto={gato1.longitud_salto}")
    Gato.sonido()
    gato2 = GatoPeloCorto("Azulito", 1, "azul", 0.8, 1.5, "azul ruso")
    print(f"GatoPeloCorto: nombre={gato2.nombre}, raza={gato2.raza}, color={gato2.color}, altura de salto={gato2.altura_salto}, longitud de salto={gato2.longitud_salto}")
    Gato.sonido()
    print("\n------- PRUEBA DE PERROS -----")
    perro1 = PerroPequeño("Toby", 2, "blanco", 5.0, False, "caniche")
    print(f"PerroPequeño: nombre={perro1.nombre}, raza={perro1.raza}, color={perro1.color}, peso={perro1.peso}kg, muerde={perro1.muerde}")
    Perro.sonido()
    perro2 = PerroMediano("Rex", 4, "marrón", 18.0, True, "dálmata")
    print(f"PerroMediano: nombre={perro2.nombre}, raza={perro2.raza}, color={perro2.color}, peso={perro2.peso}kg, muerde={perro2.muerde}")
    Perro.sonido()