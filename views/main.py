from controllers.estudiante_controller import EstudianteController
from controllers.profesor_controller import ProfesorController
from controllers.curso_controller import CursoController
from models.profesor import Profesor

if __name__ == "__main__":
    estudiante_ctrl = EstudianteController()
    profesor_ctrl = ProfesorController()
    curso_ctrl = CursoController()  # Singleton

    while True:
        print("\n📚 MENÚ DEL SISTEMA DE GESTIÓN ESCOLAR 📚")
        print("1. Agregar Estudiante")
        print("2. Listar Estudiantes")
        print("3. Agregar Profesor")
        print("4. Listar Profesores")
        print("5. Agregar Curso")
        print("6. Listar Cursos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            curso = input("Curso: ")
            print(estudiante_ctrl.agregar_estudiante(nombre, edad, curso))

        elif opcion == "2":
            print("\nLista de Estudiantes:")
            print(estudiante_ctrl.listar_estudiantes())

        elif opcion == "3":
            nombre = input("Nombre del profesor: ")
            asignatura = input("Asignatura: ")
            print(profesor_ctrl.agregar_profesor(nombre, asignatura))

        elif opcion == "4":
            print("\nLista de Profesores:")
            print(profesor_ctrl.listar_profesores())

        elif opcion == "5":
            nombre = input("Nombre del curso: ")
            codigo = input("Código del curso: ")
            profesor_nombre = input("Nombre del profesor del curso: ")

            profesor_existente = None
            for prof in profesor_ctrl.profesores:
                if prof.nombre == profesor_nombre:
                    profesor_existente = prof
                    break
            
            if profesor_existente:
                print(curso_ctrl.agregar_curso(nombre, codigo, profesor_existente))
            else:
                print("⚠️ Profesor no encontrado. Agregue el profesor primero.")

        elif opcion == "6":
            print("\nLista de Cursos:")
            print(curso_ctrl.listar_cursos())  # Asegúrate de usar la misma instancia

        elif opcion == "7":
            print("Saliendo del sistema... 🚀")
            break

        else:
            print("⚠️ Opción no válida. Inténtelo de nuevo.")