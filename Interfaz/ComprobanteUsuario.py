from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QDateTime
from Modelo.cliente import Cliente
from Modelo.venta import Venta
from Modelo.reserva import ReservaPasaje
from Modelo.reservaAsiento import ReservarAsiento
from Modelo.asiento import Asiento
from datetime import date
import random

class ComprobanteUsuario(QWidget):
    def __init__(self, asientos_seleccionados=None, nombre_cliente=None, 
                 rut_cliente=None, destino=None, embarcacion=None, 
                 fecha_viaje=None, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.asientos_seleccionados = asientos_seleccionados or []
        self.nombre_cliente = nombre_cliente
        self.rut_cliente = rut_cliente
        self.destino = destino
        self.embarcacion = embarcacion
        self.fecha_viaje = fecha_viaje
        self.patagonia_wellboat = patagonia_wellboat
        self.numero_comprobante = str(random.randint(100000, 999999))
        self.fecha_comprobante = QDateTime.currentDateTime().toString("dd/MM/yyyy HH:mm:ss")
        
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Comprobante de Compra")
        self.setGeometry(300, 50, 1000, 900)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        # Botón Volver
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.resize(80, 30)
        self.btn_volver.move(900, 20)
        self.btn_volver.clicked.connect(self.volver_atras)

        pos_y = 20

        titulo_empresa = QLabel("PATAGONIA WELLBOAT", self)
        titulo_empresa.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        titulo_empresa.move(350, pos_y)
        pos_y += 35

        # Línea divisoria
        linea1 = QLabel("-" * 80, self)
        linea1.setFont(QFont("Courier", 10))
        linea1.move(50, pos_y)
        pos_y += 20

        # Información del comprobante 
        info_comprobante = QLabel("COMPROBANTE DE COMPRA", self)
        info_comprobante.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        info_comprobante.move(400, pos_y)
        pos_y += 35

        # Número y fecha
        num_label = QLabel(f"Nº Comprobante: {self.numero_comprobante}", self)
        num_label.setFont(QFont("Arial", 10))
        num_label.move(50, pos_y)
        pos_y += 25

        fecha_label = QLabel(f"Fecha y Hora: {self.fecha_comprobante}", self)
        fecha_label.setFont(QFont("Arial", 10))
        fecha_label.move(50, pos_y)
        pos_y += 30

        linea2 = QLabel("-" * 80, self)
        linea2.setFont(QFont("Courier", 10))
        linea2.move(50, pos_y)
        pos_y += 20

        # Información del cliente
        cliente_titulo = QLabel("DATOS DEL CLIENTE", self)
        cliente_titulo.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        cliente_titulo.move(50, pos_y)
        pos_y += 25

        cliente_nombre = QLabel(f"Nombre: {self.nombre_cliente or 'N/A'}", self)
        cliente_nombre.setFont(QFont("Arial", 10))
        cliente_nombre.move(70, pos_y)
        pos_y += 25

        cliente_rut = QLabel(f"RUT: {self.rut_cliente or 'N/A'}", self)
        cliente_rut.setFont(QFont("Arial", 10))
        cliente_rut.move(70, pos_y)
        pos_y += 30

        linea3 = QLabel("-" * 80, self)
        linea3.setFont(QFont("Courier", 10))
        linea3.move(50, pos_y)
        pos_y += 20

        # Detalles del viaje
        viaje_titulo = QLabel("DETALLES DEL VIAJE", self)
        viaje_titulo.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        viaje_titulo.move(50, pos_y)
        pos_y += 25

        # Destino
        destino_nombre = self.destino.nombre if self.destino else "N/A"
        destino_label = QLabel(f"Destino: {destino_nombre}", self)
        destino_label.setFont(QFont("Arial", 10))
        destino_label.move(70, pos_y)
        pos_y += 25

        # Fecha del viaje
        fecha_label = QLabel(f"Fecha del Viaje: {self.fecha_viaje or 'N/A'}", self)
        fecha_label.setFont(QFont("Arial", 10))
        fecha_label.move(70, pos_y)
        pos_y += 25

        # Tipo de embarcación
        embarcacion_nombre = self.embarcacion.nombre if self.embarcacion else "N/A"
        embarcacion_label = QLabel(f"Embarcación: {embarcacion_nombre}", self)
        embarcacion_label.setFont(QFont("Arial", 10))
        embarcacion_label.move(70, pos_y)
        pos_y += 30

        linea4 = QLabel("-" * 80, self)
        linea4.setFont(QFont("Courier", 10))
        linea4.move(50, pos_y)
        pos_y += 20

        # Detalles de asientos
        asientos_titulo = QLabel("ASIENTOS RESERVADOS", self)
        asientos_titulo.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        asientos_titulo.move(50, pos_y)
        pos_y += 25

        # Listado de asientos
        asientos_str = ", ".join(map(str, sorted(self.asientos_seleccionados)))
        asientos_label = QLabel(f"Asientos: {asientos_str}", self)
        asientos_label.setFont(QFont("Arial", 10))
        asientos_label.move(70, pos_y)
        pos_y += 25

        # Cantidad de asientos
        cantidad = len(self.asientos_seleccionados)
        cantidad_label = QLabel(f"Cantidad: {cantidad} asiento(s)", self)
        cantidad_label.setFont(QFont("Arial", 10))
        cantidad_label.move(70, pos_y)
        pos_y += 30

        linea5 = QLabel("-" * 80, self)
        linea5.setFont(QFont("Courier", 10))
        linea5.move(50, pos_y)
        pos_y += 20

        # Cálculo de precios
        precio_unitario = self.destino.precio_pasaje if self.destino else 0
        precio_total = precio_unitario * cantidad

        precio_unitario_label = QLabel(f"Precio por asiento: ${precio_unitario:,}", self)
        precio_unitario_label.setFont(QFont("Arial", 10))
        precio_unitario_label.move(50, pos_y)
        pos_y += 25

        linea_total = QLabel("-" * 80, self)
        linea_total.setFont(QFont("Courier", 10))
        linea_total.move(50, pos_y)
        pos_y += 15

        # 
        total_label = QLabel(f"TOTAL A PAGAR: ${precio_total:,}", self)
        total_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        total_label.setStyleSheet("color: #006400;")
        total_label.move(50, pos_y)
        pos_y += 35

        linea_final = QLabel("-" * 80, self)
        linea_final.setFont(QFont("Courier", 10))
        linea_final.move(50, pos_y)
        pos_y += 25

        # Mensajes finales
        pie1 = QLabel("Gracias por su compra", self)
        pie1.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        pie1.move(400, pos_y)
        pos_y += 25

        pie2 = QLabel("Este comprobante tiene validez como recibo de pago", self)
        pie2.setFont(QFont("Arial", 9))
        pie2.move(350, pos_y)
        pos_y += 50

        # Botón Descargar/Imprimir (simulado no sirve)
        self.btn_imprimir = QPushButton("Descargar Comprobante", self)
        self.btn_imprimir.resize(150, 40)
        self.btn_imprimir.setFont(QFont("Arial", 10))
        self.btn_imprimir.move(250, pos_y)

        # Botón Finalizar (si cierra la ventana)
        self.btn_finalizar = QPushButton("Finalizar", self)
        self.btn_finalizar.resize(150, 40)
        self.btn_finalizar.setFont(QFont("Arial", 10))
        self.btn_finalizar.move(550, pos_y)
        self.btn_finalizar.clicked.connect(self.finalizar)

    def finalizar(self):
        # Guardar datos
        self.guardar_datos()
        if self.parent_window:
            self.parent_window.show()
        self.close()

    def guardar_datos(self):
        """Guarda todos los datos en las clases del modelo según el UML"""
        try:
            # 1. Crear cliente y registrarlo
            cliente = Cliente(self.nombre_cliente, self.rut_cliente)
            cliente.registrar_viaje()
            
            # 2. Guardar cliente en PatagoniaWellboat
            if self.patagonia_wellboat:
                self.patagonia_wellboat.agregar_cliente(cliente)
            
            # 3. Calcular precio total
            precio_unitario = self.destino.precio_pasaje if self.destino else 0
            precio_total = precio_unitario * len(self.asientos_seleccionados)
            
            # 4. Crear venta (referencia al cliente)
            venta = Venta(
                id=int(self.numero_comprobante),
                cliente=cliente,  # Referencia al objeto Cliente
                viaje=None,
                fecha=date.today(),
                total_paga=precio_total
            )
            
            # 5. Guardar venta en PatagoniaWellboat
            if self.patagonia_wellboat:
                self.patagonia_wellboat.agregar_venta(venta)
            
            # 6. Crear reservas de pasaje y asientos (una por cada asiento seleccionado)
            # 6. Crear UNA SOLA ReservaPasaje con TODOS los asientos seleccionados en una compra
            # Convertir asientos a string para almacenamiento
            asientos_str = ", ".join(map(str, sorted(self.asientos_seleccionados)))
        
            reserva_pasaje = ReservaPasaje(
                id=int(self.numero_comprobante),
                cliente=cliente,  # Referencia al objeto Cliente
                viaje=None,
                asiento=asientos_str  # Almacenar como string con todos los asientos
            )
            # Añadir atributos para visualización
            reserva_pasaje.asientos_lista = sorted(self.asientos_seleccionados)
            reserva_pasaje.destino = self.destino
            reserva_pasaje.fecha = self.fecha_viaje
            reserva_pasaje.precio = precio_total
        
            if self.patagonia_wellboat:
                self.patagonia_wellboat.agregar_reserva(reserva_pasaje)
        
            # 7. Crear ReservaAsiento por cada asiento (para tracking de ocupación)
            for asiento_num in self.asientos_seleccionados:
                asiento = Asiento(numero=asiento_num, ocupado=True)
                reserva_asiento = ReservarAsiento(asiento=asiento)
                if self.patagonia_wellboat:
                    self.patagonia_wellboat.agregar_reserva_asiento(reserva_asiento)
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def volver_atras(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()