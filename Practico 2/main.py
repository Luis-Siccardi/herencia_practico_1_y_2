from caja_ahorro import CajaAhorro
from cuenta_corriente import CuentaCorriente

# Programa principal
# Aca creamos objetos y probamos los métodos de cada clase.

print("CAJA DE AHORRO")

# Creamos una caja de ahorro con titular, saldo inicial e interes.
caja = CajaAhorro("Lucia", 10000, 10)

caja.consultar_saldo()
caja.depositar(2000)
caja.extraer(3000)
caja.aplicar_interes()
caja.consultar_saldo()

print("------------------------------")

print("CUENTA CORRIENTE")

# Creamos una cuenta corriente con titular, saldo inicial y comision.
cuenta = CuentaCorriente("Mateo", 15000, 500)

cuenta.consultar_saldo()
cuenta.depositar(0)
cuenta.extraer_con_comision(14000)
cuenta.consultar_saldo()



