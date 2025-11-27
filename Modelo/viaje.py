from Modelo.cliente import Cliente
from datetime import date

class Viaje:
    def __init__(self, id: int, cliente: Cliente, fecha: date, totalpago: int):
        self.id = id
        self.cliente = cliente
        self.fecha = fecha 
        self.totalpago = totalpago
