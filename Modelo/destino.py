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

#Input: Destino, cantidad de asientos
#Calculo del precio total del pasaje
#Output: precio total pasaje
def precio_total_pasaje(destino: Destino, cantidad_asientos: int) -> int:
    return destino.precio_pasaje * cantidad_asientos

#Input: Destino, peso en kg
#Calculo del precio total de la encomienda
#Output: precio total encomienda
def precio_total_encomienda(destino: Destino, peso_kg: float) -> int:
    return int(destino.precio_encomienda * peso_kg)


destino_ejemplo = DESTINOS[0]
#print(precio_total_pasaje(destino_ejemplo, 3))
print(precio_total_encomienda(destino_ejemplo, 5.5))

