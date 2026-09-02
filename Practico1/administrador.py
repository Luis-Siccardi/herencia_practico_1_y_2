# Clase hija Administrador
from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre_usuario, nombre_completo, contrasena, area):
        # Reutilizamos los atributos de Usuario
        super().__init__(nombre_usuario, nombre_completo, contrasena)
        self.area = area

    # Mostramos datos propios del administrador
    def mostrar_datos(self):
        super().mostrar_datos()
        print("Tipo de usuario: Administrador")
        print("Área:", self.area)

