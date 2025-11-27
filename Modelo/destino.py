class Destino:
    def __init__(self, nombre: str, precio_pasaje: int, precio_encomienda: int):
        self.nombre = nombre
        self.precio_pasaje = precio_pasaje
        self.precio_encomienda = precio_encomienda
DESTINOS = [
    Destino("Calbuco", 15000, 4000), 
    Destino("Maillen", 15000, 4000), 
    Destino("Isla Puluqui", 20000, 5000), 
    Destino("Achao", 25000, 6000), 
    Destino("Quinchao", 25000, 6000),
    Destino("Dalcahue", 30000, 8000), 
    Destino("Curaco de Vélez", 30000, 8000), 
    Destino("Queilen", 40000, 10000), 
    Destino("Chonchi", 40000, 10000), 
    Destino("Melinka", 50000, 12000), 
    Destino("Quellón", 50000, 12000)
]

def precio_pasaje(precio_pasaje: int) -> int:
    return precio_pasaje