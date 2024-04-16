from abc import ABC, abstractmethod

# Clase Cliente
class Cliente(ABC):
    @abstractmethod
    def crea_pedido(self):
        pass
# Creadores concretos
class ClienteContado(Cliente):
    def crea_pedido(self):
        return PedidoContado()
class ClienteCredito(Cliente):
    def crea_pedido(self):
        return PedidoCredito()
# Clase Pedido
class Pedido(ABC):
    @abstractmethod
    def pagar(self):
        pass
    @abstractmethod
    def validar(self):
        pass
# Productos concretos
class PedidoContado(Pedido):
    def pagar(self):
        return "Pagando al contado"
    def validar(self):
        return True
class PedidoCredito(Pedido):
    def pagar(self):
        return "Pagando al credito"
    def validar(self):
        return True

# Realizando pedidos

print("Cliente 1:")
cliente1 = ClienteContado()
pedido1 = cliente1.crea_pedido()
print(pedido1.pagar())
if pedido1.validar(): print("Pago realizado")
else: print("Pago rechazado")
print("*"*50)
print("Cliente 2:")
cliente2 = ClienteCredito()
pedido2 = cliente2.crea_pedido()
print(pedido2.pagar())
if pedido1.validar(): print("Pago realizado")
else: print("Pago rechazado")