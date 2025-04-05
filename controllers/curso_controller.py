from models.curso import Curso

class CursoController:
    _instance = None  # Singleton

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CursoController, cls).__new__(cls)
            cls._instance.cursos = []  # Lista en memoria para gestionar cursos
        return cls._instance

    def agregar_curso(self, nombre, codigo, profesor):
        curso = Curso(nombre, codigo, profesor)
        self.cursos.append(curso)
        return f"Curso {nombre} agregado con código {codigo}."

    def listar_cursos(self):
        if not self.cursos:
            return "No hay cursos registrados."
        return "\n".join(str(curso) for curso in self.cursos)