class Cliente:
    def __init__(self, nombre: str, rut: str, historial_viajes: int = 0, emergencia: bool = False):
        self.nombre = nombre
        self.rut = rut
        self.historial_viajes = historial_viajes
        self.emergencia = emergencia

    def es_frecuente(self) -> bool:
        return self.historial_viajes > 10

    def aplicar_descuento(self, monto: float) -> float:
        if self.es_frecuente():
            return monto * 0.9
        return monto

    def en_emergencia(self) -> bool:
        return self.emergencia

    def registrar_viaje(self):
        self.historial_viajes += 1

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "rut": self.rut,
            "historial_viajes": self.historial_viajes,
            "emergencia": self.emergencia
        }