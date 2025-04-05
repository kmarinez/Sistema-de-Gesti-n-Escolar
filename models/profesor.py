class Profesor:
    def __init__(self, nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura

    def __str__(self):
        return f"Profesor {self.nombre}, Asignatura: {self.asignatura}"
