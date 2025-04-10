from models.curso import Curso

class CursoController:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, nombre, codigo, profesor, limite=2):
        curso = Curso(nombre, codigo, profesor, limite)
        self.cursos.append(curso)
        return f"Curso {nombre} agregado con código {codigo} y límite {limite} estudiantes."

    def listar_cursos(self):
        if not self.cursos:
            return "No hay cursos registrados."
        return "\n".join(str(curso) for curso in self.cursos)