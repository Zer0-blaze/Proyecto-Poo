from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont

class VerEncomiendas(QWidget):
    def __init__(self, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.patagonia_wellboat = patagonia_wellboat
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Ver Encomiendas - Patagonia Wellboat")
        self.setGeometry(300, 100, 1100, 600)
        self.generar_formulario()
        try:
            self.cargar_encomiendas()
        except Exception as e:
            print("[VerEncomiendas] Error al cargar encomiendas:", e)
        self.show()

    def generar_formulario(self):
        # Título
        titulo = QLabel("Registro de Encomiendas", self)
        titulo.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        titulo.move(50, 20)

        # Tabla de encomiendas
        self.tabla_encomiendas = QTableWidget(self)
        self.tabla_encomiendas.setColumnCount(7)
        self.tabla_encomiendas.setHorizontalHeaderLabels(["ID", "Remitente", "Destinatario", "Destino", "Peso (kg)", "Precio", "Fecha"])
        self.tabla_encomiendas.resize(1000, 450)
        self.tabla_encomiendas.move(50, 70)
        self.tabla_encomiendas.setColumnWidth(0, 80)
        self.tabla_encomiendas.setColumnWidth(1, 150)
        self.tabla_encomiendas.setColumnWidth(2, 150)
        self.tabla_encomiendas.setColumnWidth(3, 120)
        self.tabla_encomiendas.setColumnWidth(4, 100)
        self.tabla_encomiendas.setColumnWidth(5, 100)
        self.tabla_encomiendas.setColumnWidth(6, 120)

        # Botón Cerrar
        self.btn_cerrar = QPushButton("Cerrar", self)
        self.btn_cerrar.resize(100, 35)
        self.btn_cerrar.move(950, 540)
        self.btn_cerrar.clicked.connect(self.cerrar_ventana)

    def cargar_encomiendas(self):
        try:
            if not self.patagonia_wellboat:
                return

            # Obtener todas las reservas y filtrar las encomiendas
            reservas = self.patagonia_wellboat.obtener_reservas() or []
            from Modelo.reserva import ReservaEncomienda

            encomiendas = [r for r in reservas if isinstance(r, ReservaEncomienda)]
            self.tabla_encomiendas.setRowCount(len(encomiendas))

            for fila, encomienda in enumerate(encomiendas):
                try:
                    # ID 
                    id_val = getattr(encomienda, 'id', None)
                    if not id_val:
                        # Generar ID legible si falta (EN-0001, EN-0002, ...)
                        id_val = f"EN-{fila+1:04d}"
                    item_id = QTableWidgetItem(str(id_val))
                    self.tabla_encomiendas.setItem(fila, 0, item_id)

                    # Remitente
                    remitente = getattr(encomienda, 'cliente', None)
                    remitente_nombre = remitente.nombre if remitente and hasattr(remitente, 'nombre') else "N/A"
                    item_remitente = QTableWidgetItem(remitente_nombre)
                    self.tabla_encomiendas.setItem(fila, 1, item_remitente)

                    # Destinatario
                    destinatario = getattr(encomienda, 'destinatario', getattr(encomienda, 'destinatario', 'N/A'))
                    item_destinatario = QTableWidgetItem(str(destinatario))
                    self.tabla_encomiendas.setItem(fila, 2, item_destinatario)

                    # Destino
                    destino_obj = getattr(encomienda, 'destino', None)
                    destino_nombre = destino_obj.nombre if destino_obj and hasattr(destino_obj, 'nombre') else "N/A"
                    item_destino = QTableWidgetItem(str(destino_nombre))
                    self.tabla_encomiendas.setItem(fila, 3, item_destino)

                    # Peso (puede almacenarse como 'peso' o 'pesoKg')
                    peso_val = getattr(encomienda, 'peso', getattr(encomienda, 'pesoKg', 'N/A'))
                    item_peso = QTableWidgetItem(str(peso_val))
                    self.tabla_encomiendas.setItem(fila, 4, item_peso)

                    # Precio
                    precio_val = getattr(encomienda, 'precio', None)
                    if isinstance(precio_val, (int, float)):
                        precio = f"${precio_val:,}"
                    else:
                        precio = str(precio_val) if precio_val is not None else "N/A"
                    item_precio = QTableWidgetItem(precio)
                    self.tabla_encomiendas.setItem(fila, 5, item_precio)

                    # Fecha
                    fecha_val = getattr(encomienda, 'fecha', None)
                    item_fecha = QTableWidgetItem(str(fecha_val) if fecha_val is not None else "-")
                    self.tabla_encomiendas.setItem(fila, 6, item_fecha)
                except Exception as row_e:
                    print("[VerEncomiendas] Error procesando fila de encomienda:", row_e)
                    # Rellenar fila con valores por defecto en caso de error
                    for col in range(7):
                        self.tabla_encomiendas.setItem(fila, col, QTableWidgetItem("N/A"))
        except Exception as e:
            print("[VerEncomiendas] Error general al cargar encomiendas:", e)

    def cerrar_ventana(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()
