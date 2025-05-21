from Estudiante import Estudiante
from Profesor import Profesor

def main():
    est = Estudiante("Alejandro", "Calle Falsa 123", "Ingeniería Sistemas", 3)
    print(f"Estudiante: {est.getNombre()}, Carrera: {est.getCarrera()}, Semestre: {est.getSemestre()}")

    prof = Profesor("Maxwell", "Av. Principal 456", "Física", "Titular")
    print(f"Profesor: {prof.getNombre()}, Departamento: {prof.getDepartamento()}, Categoría: {prof.getCategoria()}")

if __name__ == "__main__":
    main()