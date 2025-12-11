from datetime import datetime
from Modelo.cliente import Cliente
from Modelo.viaje import Viaje

class Reserva:
    def __init__(self, id_reserva= int, cliente= Cliente, viaje= Viaje, precio_final= int):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.viaje = viaje
        self.precio_final = precio_final

    def calcularPrecioFinal(self):
        
        pass

    def confirmarReserva(self):
        pass

    def cancelarReserva(self):
        pass

class ReservaEncomienda(Reserva):
    def __init__(self, id: int, cliente, viaje, pesoKg: float, fechaEstimadaEntrega= datetime):
        super().__init__(id, cliente, viaje)
        self.pesoKg = pesoKg
        self.fechaEstimadaEntrega = fechaEstimadaEntrega

    def calcularpreciopeso(self):
        pass

class ReservaPasaje(Reserva):
    
    def __init__(self, id: int, cliente, viaje, asiento=None):
        super().__init__(id, cliente, viaje)
        self.asiento = asiento

    def seleccionarAsiento(self, asiento) -> bool:
        if asiento.ocupado:
            return False

        self.asiento = asiento
        asiento.marcarOcupado()
        return True
    