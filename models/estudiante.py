class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, Curso: {self.curso}"
