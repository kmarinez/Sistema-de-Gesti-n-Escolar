from models.profesor import Profesor

class ProfesorController:
    def __init__(self):
        self.profesores = []

    def agregar_profesor(self, nombre, asignatura):
        profesor = Profesor(nombre, asignatura)
        self.profesores.append(profesor)
        return f"Profesor {nombre} agregado con asignatura {asignatura}."

    def listar_profesores(self):
        if not self.profesores:
            return "No hay profesores registrados."
        return "\n".join(str(prof) for prof in self.profesores)
