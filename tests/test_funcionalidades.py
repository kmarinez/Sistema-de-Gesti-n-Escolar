import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.estudiante_controller import EstudianteController
from controllers.profesor_controller import ProfesorController
from controllers.curso_controller import CursoController
from models.profesor import Profesor
from models.curso import Curso

# ---------------- PRUEBAS UNITARIAS ----------------

def test_registrar_estudiante_valido():
    ctrl = EstudianteController()
    resultado = ctrl.agregar_estudiante("Ana", 20, "Matemática")
    assert "Ana" in resultado

def test_registrar_estudiante_duplicado():
    ctrl = EstudianteController()
    ctrl.agregar_estudiante("Ana", 20, "Matemática")
    resultado = ctrl.agregar_estudiante("Ana", 20, "Matemática")
    assert "ya está registrado" in resultado

# ---------------- PRUEBAS DE INTEGRACIÓN ----------------

def test_inscribir_estudiante_en_curso_valido():
    profesor_ctrl = ProfesorController()
    curso_ctrl = CursoController()
    estudiante_ctrl = EstudianteController()

    profesor_ctrl.agregar_profesor("Luis", "Matemática")
    profesor = profesor_ctrl.profesores[0]

    curso_ctrl.agregar_curso("Matemática", "MAT101", profesor, limite=2)
    estudiante_ctrl.agregar_estudiante("Ana", 20, "Matemática")

    curso = curso_ctrl.cursos[0]
    estudiante = estudiante_ctrl.estudiantes[0]
    resultado = curso.agregar_estudiante(estudiante)

    assert "inscrito correctamente" in resultado

def test_inscribir_en_curso_lleno():
    profesor = Profesor("Luis", "Historia")
    curso = Curso("Historia", "HIS101", profesor, limite=1)

    class DummyEstudiante:
        def __init__(self, nombre):
            self.nombre = nombre

    estudiante1 = DummyEstudiante("Ana")
    estudiante2 = DummyEstudiante("Laura")

    curso.agregar_estudiante(estudiante1)
    resultado = curso.agregar_estudiante(estudiante2)

    assert "Curso lleno" in resultado
    assert len(curso.estudiantes) == 1

# ---------------- PRUEBAS DE AUTENTICACIÓN ----------------

class FakeLoginSystem:
    def __init__(self):
        self.usuarios = {"admin": "1234"}
        self.intentos_fallidos = {}

    def login(self, usuario, contrasena):
        if usuario not in self.intentos_fallidos:
            self.intentos_fallidos[usuario] = 0

        if self.intentos_fallidos[usuario] >= 6:
            return "Cuenta bloqueada temporalmente"

        if self.usuarios.get(usuario) == contrasena:
            return "Acceso concedido"
        else:
            self.intentos_fallidos[usuario] += 1
            return "Credenciales inválidas"

def test_inicio_sesion_credenciales_validas():
    sistema = FakeLoginSystem()
    resultado = sistema.login("admin", "1234")
    assert resultado == "Acceso concedido"

def test_inicio_sesion_6_intentos_fallidos():
    sistema = FakeLoginSystem()
    for _ in range(6):
        sistema.login("admin", "malclave")

    resultado = sistema.login("admin", "malclave")
    assert resultado == "Cuenta bloqueada temporalmente"