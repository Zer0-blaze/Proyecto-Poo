from Modelo.cliente import Cliente
from Modelo.viaje import Viaje
from datetime import date
class Venta:

    def __init__(self, id: int, cliente: Cliente, viaje = Viaje, fecha = date, total_paga= int):
        self.id = id
        self.cliente = cliente
        self.viaje = viaje
        self.fecha = fecha
        self.total_paga = total_paga