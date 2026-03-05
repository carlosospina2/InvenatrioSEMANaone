from validacion_entrada import validar_monto
from historial import historial_operaciones


def menu(cuenta):
    print("=" * 40)
    print("                 Menu")
    print("=" * 40)
    print("1- Consultar Saldo")
    print("2- Retiro de saldo")
    print("3- Depositar Dinero")
    Ejecucion = int(input("Elija una opcion"))
