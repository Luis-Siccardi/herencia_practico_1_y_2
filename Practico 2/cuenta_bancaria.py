class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular

        # El saldo queda encapsulado, no se debe modificar directamente desde afuera.
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        # Este metodo permite ver el saldo sin acceder directamente al atributo.
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.__saldo}")

    def depositar(self, monto):
        # Solo se puede depositar si el monto es mayor que cero.
        if monto > 0:
            self.__saldo += monto
            print(f"Deposito realizado: ${monto}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def extraer(self, monto):
        # Solo se puede extraer si hay saldo suficiente.
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Extraccion realizada: ${monto}")
        else:
            print("No se puede realizar la extraccion.")

    def _obtener_saldo(self):
        # Metodo protegido para que las clases hijas puedan consultar el saldo.
        return self.__saldo

    def _modificar_saldo(self, monto):
        # Metodo protegido para que las clases hijas puedan cambiar el saldo.
        self.__saldo += monto
