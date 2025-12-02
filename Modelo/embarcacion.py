class Embarcacion:
    def __init__(self, nombre: str, capacidadPasajeros: int, capacidadCargaKg: float, layout=None):
        self.nombre = nombre
        self.capacidadPasajeros = capacidadPasajeros
        self.capacidadCargaKg = capacidadCargaKg
        self.layout_asientos = layout
        self.asientos_ocupados = set()

    def obtenerCapacidadPasajeros(self) -> int:
        return self.capacidadPasajeros

    def obtenerCapacidadCarga(self) -> float:
        return self.capacidadCargaKg

    def puedeRealizarViaje(self, pasajeros: int, cargaKg: float) -> bool:
        return (
            pasajeros <= self.capacidadPasajeros and
            cargaKg <= self.capacidadCargaKg
        )

    @staticmethod

#Input: lista de embarcaciones, cantidad de pasajeros, carga en kg
#Selecciona la primera embarcación que pueda realizar el viaje, esto en función de su capacidad
#Output: embarcación seleccionada o None si no hay ninguna que pueda realizar el viaje
    def seleccionarEmbarcacion(embarcaciones, pasajeros: int, cargaKg: float):
        for barco in embarcaciones:
            if barco.puedeRealizarViaje(pasajeros, cargaKg):
                return barco
        return None
    
    #Input: id del asiento
    #Verifica si un asiento está disponible
    #Output: booleano indicando si el asiento está disponible
    def es_asiento_disponible(self, asiento_id: str) -> bool:
        return asiento_id not in self.asientos_ocupados
    
    #Input: id del asiento
    #Marca un asiento como ocupado si está disponible
    #Output: booleano indicando si la operación fue exitosa
    def ocupar_asiento(self, asiento_id: str):
        if self.es_asiento_disponible(asiento_id):
            self.asientos_ocupados.add(asiento_id)
            return True
        return False  
    
#Input: ninguna
#
#Output: representación en cadena de la embarcación
    def __str__(self):
        return (
            f"Embarcación: {self.nombre}\n"
            f"Capacidad Pasajeros: {self.capacidadPasajeros}\n"
            f"Capacidad Carga (kg): {self.capacidadCargaKg}"
        )


class CatamaranLiviano(Embarcacion):
    def __init__(self, nombre="Catamarán Liviano"):
        super().__init__(nombre, capacidadPasajeros=20, capacidadCargaKg=1000)


class FerryMediano(Embarcacion):
    def __init__(self, nombre="Ferry Mediano"):
        super().__init__(nombre, capacidadPasajeros=50, capacidadCargaKg=3500)


class WellboatGranCapacidad(Embarcacion):
    def __init__(self, nombre="Wellboat Gran Capacidad"):
        super().__init__(nombre, capacidadPasajeros=80, capacidadCargaKg=5000)
