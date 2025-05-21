from Estudiante import Estudiante
from Profesor import Profesor

def main():
    est = Estudiante("Alejandro", "Por la Candelaria", "Ingeniería Sistemas", 2)
    print(f"Estudiante: {est.getNombre()},Dirección:{est.getDireccion()},Carrera: {est.getCarrera()}, Semestre: {est.getSemestre()}")

    prof = Profesor("Maxwell", "Por Belén", "Ciencias", "Titular")
    print(f"Profesor: {prof.getNombre()},Dirección:{prof.getDireccion()},Departamento: {prof.getDepartamento()}, Categoría: {prof.getCategoria()}")

if __name__ == "__main__":
    main()