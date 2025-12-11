from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox
from PyQt6.QtGui import QFont
from Interfaz.ComprobanteEncomienda import ComprobanteEncomienda

class DetallesEncomienda(QWidget):
    def __init__(self, remitente=None, destinatario=None, destino=None, 
                 peso=None, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.patagonia_wellboat = patagonia_wellboat
        self.remitente = remitente
        self.destinatario = destinatario
        self.destino = destino
        self.peso = peso
        
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Detalles Encomienda")
        self.setGeometry(400, 100, 900, 700)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        # Botón Cancelar
        self.btn_cancelar = QPushButton("Cancelar", self)
        self.btn_cancelar.resize(120, 35)
        self.btn_cancelar.move(750, 20)
        self.btn_cancelar.clicked.connect(self.cancelar)

        # Título
        titulo = QLabel("Resumen de Encomienda", self)
        titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        titulo.move(50, 70)

        pos_y = 120
        espaciado = 35

        # Datos del Remitente
        label_titulo_remitente = QLabel("Datos del Remitente", self)
        label_titulo_remitente.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label_titulo_remitente.move(50, pos_y)
        pos_y += espaciado

        label_remitente = QLabel(f"Remitente: {self.remitente or 'N/A'}", self)
        label_remitente.setFont(QFont("Arial", 11))
        label_remitente.move(50, pos_y)
        pos_y += espaciado

        # Datos del Destinatario
        pos_y += 10
        label_titulo_destinatario = QLabel("Datos del Destinatario", self)
        label_titulo_destinatario.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label_titulo_destinatario.move(50, pos_y)
        pos_y += espaciado

        label_destinatario = QLabel(f"Destinatario: {self.destinatario or 'N/A'}", self)
        label_destinatario.setFont(QFont("Arial", 11))
        label_destinatario.move(50, pos_y)
        pos_y += espaciado

        # Detalles de la Encomienda
        pos_y += 10
        label_titulo_detalle = QLabel("Detalles de la Encomienda", self)
        label_titulo_detalle.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label_titulo_detalle.move(50, pos_y)
        pos_y += espaciado

        # Destino
        destino_nombre = self.destino.nombre if self.destino else "N/A"
        label_destino = QLabel(f"Destino: {destino_nombre}", self)
        label_destino.setFont(QFont("Arial", 11))
        label_destino.move(50, pos_y)
        pos_y += espaciado

        # Peso
        label_peso = QLabel(f"Peso: {self.peso} kg", self)
        label_peso.setFont(QFont("Arial", 11))
        label_peso.move(50, pos_y)
        pos_y += espaciado

        # Información de Precio
        pos_y += 10
        label_titulo_precio = QLabel("Información de Precio", self)
        label_titulo_precio.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label_titulo_precio.move(50, pos_y)
        pos_y += espaciado

        # Precio por kg
        precio_por_kg = self.destino.precio_encomienda if self.destino else 0
        label_precio_kg = QLabel(f"Precio por kg: ${precio_por_kg:,}", self)
        label_precio_kg.setFont(QFont("Arial", 11))
        label_precio_kg.move(50, pos_y)
        pos_y += espaciado

        # Precio total
        precio_total = precio_por_kg * self.peso if self.peso else 0
        label_precio_total = QLabel(f"PRECIO TOTAL: ${precio_total:,}", self)
        label_precio_total.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        label_precio_total.setStyleSheet("color: #006400; background-color: #e8f5e9; padding: 10px; border-radius: 5px;")
        label_precio_total.move(50, pos_y)
        label_precio_total.resize(400, 50)
        pos_y += 70

        # Botón Procesar Compra
        self.btn_procesar_compra = QPushButton("Procesar Compra", self)
        self.btn_procesar_compra.resize(200, 50)
        self.btn_procesar_compra.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.btn_procesar_compra.setStyleSheet(
            "background-color: #4CAF50; color: white; border-radius: 5px;"
        )
        procesar_x = int((self.width() - 200) / 2)
        self.btn_procesar_compra.move(procesar_x, pos_y)
        self.btn_procesar_compra.clicked.connect(self.procesar_compra)

    def procesar_compra(self):
        precio_por_kg = self.destino.precio_encomienda if self.destino else 0
        precio_total = precio_por_kg * self.peso if self.peso else 0
        
        QMessageBox.information(
            self, 
            "Compra Procesada", 
            f"¡Compra procesada exitosamente!\n\nPeso: {self.peso} kg\nTotal: ${precio_total:,}"
        )
        # Abrir ventana de comprobante
        self.ventana_comprobante = ComprobanteEncomienda(
            remitente=self.remitente,
            destinatario=self.destinatario,
            destino=self.destino,
            peso=self.peso,
            patagonia_wellboat=self.patagonia_wellboat,
            parent=self.parent_window
        )
        self.ventana_comprobante.show()
        self.close()

    def cancelar(self):
        if self.parent_window:
            self.parent_window.show()
            self.close()
        else:
            self.close()