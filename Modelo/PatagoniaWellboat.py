from Modelo.viaje import Viaje
from Modelo.embarcacion import Embarcacion
from Modelo.cliente import Cliente
from Modelo.venta import Venta

class PatagoniaWellboat:
    def __init__(self):
        self.lista_viajes = []
        self.lista_embarcaciones = []
        self.lista_clientes = []
        self.registro_ventas = []

    def agregar_viaje(self, viaje: Viaje):
        self.lista_viajes.append(viaje)

    def agregar_embarcacion(self, embarcacion: Embarcacion):
        self.lista_embarcaciones.append(embarcacion)

    def agregar_cliente(self, cliente: Cliente):
        self.lista_clientes.append(cliente)

    def agregar_venta(self, venta: Venta):
        self.registro_ventas.append(venta)

    def obtener_viajes(self):
        return self.lista_viajes

    def obtener_embarcaciones(self):
        return self.lista_embarcaciones

    def obtener_clientes(self):
        return self.lista_clientes

    def obtener_ventas(self):
        return self.registro_ventas