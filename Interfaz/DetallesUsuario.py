from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from Interfaz.ComprobanteUsuario import ComprobanteUsuario

class DetallesUsuario(QWidget):
    def __init__(self, asientos_seleccionados=None, patagonia_wellboat=None, 
                 destino=None, nombre_cliente=None, rut_cliente=None, 
                 fecha_viaje=None, embarcacion=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.asientos_seleccionados = asientos_seleccionados or []
        self.patagonia_wellboat = patagonia_wellboat
        self.destino = destino
        self.nombre_cliente = nombre_cliente
        self.rut_cliente = rut_cliente
        self.fecha_viaje = fecha_viaje
        self.embarcacion = embarcacion
        
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Detalles Compra")
        self.setGeometry(400, 100, 900, 700)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        # Botón Cancelar Compra
        self.btn_cerrar_compra = QPushButton("Cancelar Compra", self)
        self.btn_cerrar_compra.resize(120, 35)
        self.btn_cerrar_compra.move(750, 20)
        self.btn_cerrar_compra.clicked.connect(self.cerrar_compra)

        # Título
        titulo = QLabel("Resumen de Compra", self)
        titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        titulo.move(50, 70)

        pos_y = 120
        espaciado = 35

        #información del cliente
        label_titulo_cliente = QLabel("Datos del cliente", self)
        label_titulo_cliente.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label_titulo_cliente.move(50, pos_y)
        pos_y += espaciado

        # Nombre
        label_nombre = QLabel(f"Nombre: {self.nombre_cliente or 'N/A'}", self)
        label_nombre.setFont(QFont("Arial", 11))
        label_nombre.move(50, pos_y)
        pos_y += espaciado

        # RUT
        label_rut = QLabel(f"RUT: {self.rut_cliente or 'N/A'}", self)
        label_rut.setFont(QFont("Arial", 11))
        label_rut.move(50, pos_y)
        pos_y += espaciado

        # Detalles del viaje
        pos_y += 10
        label_titulo_viaje = QLabel("Detalle del viaje", self)
        label_titulo_viaje.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label_titulo_viaje.move(50, pos_y)
        pos_y += espaciado

        # Destino
        destino_nombre = self.destino.nombre if self.destino else "N/A"
        label_destino = QLabel(f"Destino: {destino_nombre}", self)
        label_destino.setFont(QFont("Arial", 11))
        label_destino.move(50, pos_y)
        pos_y += espaciado

        # Fecha
        label_fecha = QLabel(f"Fecha del viaje: {self.fecha_viaje or 'N/A'}", self)
        label_fecha.setFont(QFont("Arial", 11))
        label_fecha.move(50, pos_y)
        pos_y += espaciado

        # Embarcación
        embarcacion_nombre = self.embarcacion.nombre if self.embarcacion else "N/A"
        label_embarcacion = QLabel(f"Embarcación: {embarcacion_nombre}", self)
        label_embarcacion.setFont(QFont("Arial", 11))
        label_embarcacion.move(50, pos_y)
        pos_y += espaciado

        # Detalles de asientos
        pos_y += 10
        label_titulo_asientos = QLabel("ASIENTOS Y PRECIO", self)
        label_titulo_asientos.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label_titulo_asientos.move(50, pos_y)
        pos_y += espaciado

        # Asientos
        asientos_str = ", ".join(map(str, sorted(self.asientos_seleccionados)))
        label_asientos = QLabel(f"Asientos seleccionados: {asientos_str}", self)
        label_asientos.setFont(QFont("Arial", 11))
        label_asientos.move(50, pos_y)
        pos_y += espaciado

        # Cantidad de asientos
        cantidad_asientos = len(self.asientos_seleccionados)
        label_cantidad = QLabel(f"Cantidad de asientos: {cantidad_asientos}", self)
        label_cantidad.setFont(QFont("Arial", 11))
        label_cantidad.move(50, pos_y)
        pos_y += espaciado

        # Precio por asiento
        precio_unitario = self.destino.precio_pasaje if self.destino else 0
        label_precio_unitario = QLabel(f"Precio por asiento: ${precio_unitario:,}", self)
        label_precio_unitario.setFont(QFont("Arial", 11))
        label_precio_unitario.move(50, pos_y)
        pos_y += espaciado + 10

        # Precio total (destacado)
        precio_total = precio_unitario * cantidad_asientos
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
        QMessageBox.information(
            self, 
            "Compra Procesada", 
            f"¡Compra procesada exitosamente!\n\nAsientos: {', '.join(map(str, sorted(self.asientos_seleccionados)))}\nTotal: ${len(self.asientos_seleccionados) * (self.destino.precio_pasaje if self.destino else 0):,}"
        )
        # Abrir ventana de comprobante
        self.ventana_comprobante = ComprobanteUsuario(
            asientos_seleccionados=self.asientos_seleccionados,
            nombre_cliente=self.nombre_cliente,
            rut_cliente=self.rut_cliente,
            destino=self.destino,
            embarcacion=self.embarcacion,
            fecha_viaje=self.fecha_viaje,
            patagonia_wellboat=self.patagonia_wellboat,
            parent=self.parent_window
        )
        self.ventana_comprobante.show()
        self.close()

    def cerrar_compra(self):
        if self.parent_window:
            self.parent_window.show()
            self.close()
        else:
            self.close()