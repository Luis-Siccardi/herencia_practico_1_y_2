# Clase padre Usuario
# Clase hija Estudiante
# Clase hija Administrador
# Clase para manejar el sistema de usuarios

from estudiante import Estudiante
from administrador import Administrador


class SistemaUsuarios:
    def __init__(self):
        # Lista donde se guardan todos los usuarios registrados
        self.usuarios = []

    def buscar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return usuario
        return None

    def registrar_usuario(self, usuario):
        if self.buscar_usuario(usuario.nombre_usuario):
            print("Ese nombre de usuario ya existe.")
            return

        self.usuarios.append(usuario)
        print("Usuario registrado correctamente.")

    def iniciar_sesion(self, nombre_usuario, contrasena):
        # Recorremos la lista buscando el usuario
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                # La contrasena solo se verifica con un metodo
                if usuario.verificar_contrasena(contrasena):
                    print("\nInicio de sesion correcto.")
                    usuario.mostrar_datos()
                    return

                print("Contrasena incorrecta.")
                return

        print("Usuario no encontrado.")

    def mostrar_usuarios(self):
        if len(self.usuarios) == 0:
            print("No hay usuarios registrados.")
            return

        print("\n--- USUARIOS REGISTRADOS ---")

        for usuario in self.usuarios:
            usuario.mostrar_datos()
            print("--------------------")


def registrar_desde_menu(sistema):
    print("\n--- REGISTRO ---")
    nombre_usuario = input("Nombre de usuario: ")
    nombre_completo = input("Nombre completo: ")
    contrasena = input("Contrasena: ")

    while True:
        print("\nTipo de usuario")
        print("1. Estudiante")
        print("2. Administrador")
        tipo = input("Opcion: ").strip()

        if tipo == "1":
            curso = input("Curso: ")
            usuario = Estudiante(nombre_usuario, nombre_completo, contrasena, curso)
            sistema.registrar_usuario(usuario)
            return

        if tipo == "2":
            area = input("Area: ")
            usuario = Administrador(nombre_usuario, nombre_completo, contrasena, area)
            sistema.registrar_usuario(usuario)
            return

        print("Opcion invalida.")


def login_desde_menu(sistema):
    print("\n--- LOGIN ---")
    nombre_usuario = input("Nombre de usuario: ")
    contrasena = input("Contrasena: ")
    sistema.iniciar_sesion(nombre_usuario, contrasena)


def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Login")
    print("2. Registrarse")
    print("3. Mostrar datos")
    print("4. Salir")


def main():
    sistema = SistemaUsuarios()
    while True:
        mostrar_menu()
        opcion = input("Opcion: ").strip()
        if opcion == "1":
            login_desde_menu(sistema)
        elif opcion == "2":
            registrar_desde_menu(sistema)
        elif opcion == "3":
            sistema.mostrar_usuarios()
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opcion invalida.")

main()
