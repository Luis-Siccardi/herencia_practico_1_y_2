# Clase padre

class Usuario:
    def __init__(self, nombre_usuario, nombre_completo, contrasena):
        self.nombre_usuario = nombre_usuario
        self.nombre_completo = nombre_completo

        # La contraseña queda encapsulada.
        # No se debe acceder directamente desde afuera de la clase.
        self.__contrasena = contrasena

    # Método para verificar si la contraseña ingresada es correcta
    def verificar_contrasena(self, contrasena_ingresada):
        return self.__contrasena == contrasena_ingresada

    # Método general para mostrar datos
    def mostrar_datos(self):
        print("Usuario:", self.nombre_usuario)
        print("Nombre completo:", self.nombre_completo)
