from Modelo.destino import Destino
class encomienda:

    def __init__(self, pesoKg: float, destino: Destino, precio: int):
        self.pesoKg = pesoKg
        self.destino = destino
        self.precio = precio