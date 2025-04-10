from models.estudiante import Estudiante

class EstudianteController:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, edad, curso):
        for est in self.estudiantes:
            if est.nombre == nombre:
                return f"Error: El estudiante {nombre} ya está registrado."
        estudiante = Estudiante(nombre, edad, curso)
        self.estudiantes.append(estudiante)
        return f"Estudiante {nombre} agregado al curso {curso}."

    def listar_estudiantes(self):
        if not self.estudiantes:
            return "No hay estudiantes registrados."
        return "\n".join(str(est) for est in self.estudiantes)