# Clase hija Estudiante

from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre_usuario, nombre_completo, contrasena, curso):
        # super() llama al constructor de la clase padre Usuario
        super().__init__(nombre_usuario, nombre_completo, contrasena)
        self.curso = curso

    # Sobrescribimos el método para mostrar también el curso
    def mostrar_datos(self):
        super().mostrar_datos()
        print("Tipo de usuario: Estudiante")
        print("Curso:", self.curso)