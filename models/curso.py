class Curso:
    def __init__(self, nombre, codigo, profesor, limite=2):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.limite = limite  # Límite de estudiantes por curso
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if len(self.estudiantes) >= self.limite:
            return f"Curso lleno: no se puede inscribir a {estudiante.nombre}"
        self.estudiantes.append(estudiante)
        return f"{estudiante.nombre} inscrito correctamente en {self.nombre}"

    def __str__(self):
        return f"Curso: {self.nombre} ({self.codigo}), Profesor: {self.profesor.nombre}, Inscritos: {len(self.estudiantes)}/{self.limite}"