from cuenta_bancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, comision):
        # super() llama al __init__ de la clase padre.
        super().__init__(titular, saldo_inicial)
        self.comision = comision

    def extraer_con_comision(self, monto):
        # En la cuenta corriente se descuenta el monto mas una comision.
        total_a_descontar = monto + self.comision

        if monto > 0 and total_a_descontar <= self._obtener_saldo():
            self._modificar_saldo(-total_a_descontar)
            print(f"Extraccion realizada: ${monto}")
            print(f"Comision cobrada: ${self.comision}")
            print(f"Total descontado: ${total_a_descontar}")
        else:
            print("No se puede realizar la extraccion con comision.")
