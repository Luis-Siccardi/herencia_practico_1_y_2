from cuenta_bancaria import CuentaBancaria

class CajaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, interes):
        # super() llama al __init__ de la clase padre.
        super().__init__(titular, saldo_inicial)
        self.interes = interes

    def aplicar_interes(self):
        # Calculamos la ganancia usando el saldo actual.
        saldo = self._obtener_saldo()
        ganancia = saldo * self.interes / 100

        # Sumamos la ganancia al saldo.
        self._modificar_saldo(ganancia)

        print(f"Interes aplicado: ${ganancia}")
