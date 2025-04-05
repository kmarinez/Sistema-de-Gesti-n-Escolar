class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def __str__(self):
        return f"Curso: {self.nombre} ({self.codigo}), Profesor: {self.profesor.nombre}"
