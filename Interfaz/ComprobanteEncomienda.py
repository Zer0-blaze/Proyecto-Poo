from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QDateTime
from Modelo.cliente import Cliente
from Modelo.venta import Venta
from Modelo.reserva import ReservaEncomienda
from Modelo.encomienda import encomienda
from datetime import date, datetime
import random

class ComprobanteEncomienda(QWidget):
    def __init__(self, remitente=None, destinatario=None, destino=None, 
                 peso=None, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.remitente = remitente
        self.destinatario = destinatario
        self.destino = destino
        self.peso = peso
        self.patagonia_wellboat = patagonia_wellboat
        self.numero_comprobante = str(random.randint(100000, 999999))
        self.fecha_comprobante = QDateTime.currentDateTime().toString("dd/MM/yyyy HH:mm:ss")
        
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Comprobante de Encomienda")
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

        # Título empresa
        titulo_empresa = QLabel("PATAGONIA WELLBOAT", self)
        titulo_empresa.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        titulo_empresa.move(350, pos_y)
        pos_y += 35

        # Línea divisoria
        linea1 = QLabel("─" * 80, self)
        linea1.setFont(QFont("Courier", 10))
        linea1.move(50, pos_y)
        pos_y += 20

        # Información del comprobante 
        info_comprobante = QLabel("COMPROBANTE DE ENCOMIENDA", self)
        info_comprobante.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        info_comprobante.move(380, pos_y)
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

        # Línea divisoria
        linea2 = QLabel("─" * 80, self)
        linea2.setFont(QFont("Courier", 10))
        linea2.move(50, pos_y)
        pos_y += 20

        # Información del remitente
        remitente_titulo = QLabel("DATOS DEL REMITENTE", self)
        remitente_titulo.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        remitente_titulo.move(50, pos_y)
        pos_y += 25

        remitente_label = QLabel(f"Remitente: {self.remitente or 'N/A'}", self)
        remitente_label.setFont(QFont("Arial", 10))
        remitente_label.move(70, pos_y)
        pos_y += 30

        # Línea divisoria
        linea3 = QLabel("─" * 80, self)
        linea3.setFont(QFont("Courier", 10))
        linea3.move(50, pos_y)
        pos_y += 20

        # Información del destinatario
        destinatario_titulo = QLabel("DATOS DEL DESTINATARIO", self)
        destinatario_titulo.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        destinatario_titulo.move(50, pos_y)
        pos_y += 25

        destinatario_label = QLabel(f"Destinatario: {self.destinatario or 'N/A'}", self)
        destinatario_label.setFont(QFont("Arial", 10))
        destinatario_label.move(70, pos_y)
        pos_y += 30

        # Línea divisoria
        linea4 = QLabel("─" * 80, self)
        linea4.setFont(QFont("Courier", 10))
        linea4.move(50, pos_y)
        pos_y += 20

        # Detalles de la encomienda
        encomienda_titulo = QLabel("DETALLES DE LA ENCOMIENDA", self)
        encomienda_titulo.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        encomienda_titulo.move(50, pos_y)
        pos_y += 25

        # Destino
        destino_nombre = self.destino.nombre if self.destino else "N/A"
        destino_label = QLabel(f"Destino: {destino_nombre}", self)
        destino_label.setFont(QFont("Arial", 10))
        destino_label.move(70, pos_y)
        pos_y += 25

        # Peso
        peso_label = QLabel(f"Peso: {self.peso} kg", self)
        peso_label.setFont(QFont("Arial", 10))
        peso_label.move(70, pos_y)
        pos_y += 30

        # Línea divisoria
        linea5 = QLabel("─" * 80, self)
        linea5.setFont(QFont("Courier", 10))
        linea5.move(50, pos_y)
        pos_y += 20

        # Cálculo de precios
        precio_por_kg = self.destino.precio_encomienda if self.destino else 0
        precio_total = precio_por_kg * self.peso if self.peso else 0

        precio_kg_label = QLabel(f"Precio por kg: ${precio_por_kg:,}", self)
        precio_kg_label.setFont(QFont("Arial", 10))
        precio_kg_label.move(50, pos_y)
        pos_y += 25

        # Línea para total
        linea_total = QLabel("─" * 80, self)
        linea_total.setFont(QFont("Courier", 10))
        linea_total.move(50, pos_y)
        pos_y += 15

        # Total a pagar
        total_label = QLabel(f"TOTAL A PAGAR: ${precio_total:,}", self)
        total_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        total_label.setStyleSheet("color: #006400;")
        total_label.move(50, pos_y)
        pos_y += 35

        # Línea final
        linea_final = QLabel("═" * 80, self)
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

        # Botón Descargar
        self.btn_descargar = QPushButton("Descargar Comprobante", self)
        self.btn_descargar.resize(150, 40)
        self.btn_descargar.setFont(QFont("Arial", 10))
        self.btn_descargar.move(250, pos_y)
        self.btn_descargar.clicked.connect(self.descargar_comprobante)

        # Botón Finalizar
        self.btn_finalizar = QPushButton("Finalizar", self)
        self.btn_finalizar.resize(150, 40)
        self.btn_finalizar.setFont(QFont("Arial", 10))
        self.btn_finalizar.move(550, pos_y)
        self.btn_finalizar.clicked.connect(self.finalizar)

    def descargar_comprobante(self):
        # Aquí iría la lógica para descargar el comprobante
        pass

    def finalizar(self):
        # Guardar datos
        self.guardar_datos()
        if self.parent_window:
            self.parent_window.show()
        self.close()

    #Función para guardar los datos de la encomienda, venta y cliente
    def guardar_datos(self):
        try:
            cliente = Cliente(self.remitente, "S/N")
            # 1. Verificar si el cliente ya existe
            if self.patagonia_wellboat:
                self.patagonia_wellboat.agregar_cliente(cliente)
            
            # 3. Calcular precio total
            precio_por_kg = self.destino.precio_encomienda if self.destino else 0
            precio_total = precio_por_kg * self.peso if self.peso else 0
            
            # 4. Crear objeto Encomienda (contiene peso, destino, precio)
            encomienda_obj = encomienda(
                pesoKg=self.peso,
                destino=self.destino,
                precio=precio_total
            )
            
            # 5. Crear Venta (referencia al cliente)
            venta = Venta(
                id=int(self.numero_comprobante),
                cliente=cliente,  
                viaje=None,
                fecha=date.today(),
                total_paga=precio_total
            )
            
            # 6. Guardar venta en PatagoniaWellboat
            if self.patagonia_wellboat:
                self.patagonia_wellboat.agregar_venta(venta)
            
            # 7. Crear ReservaEncomienda (referencia a cliente + encomienda)
            reserva_encomienda = ReservaEncomienda(
                id=int(self.numero_comprobante),
                cliente=cliente, 
                viaje=None,
                pesoKg=self.peso,
                fechaEstimadaEntrega=datetime.now()
            )
            
            # 8. Guardar reserva de encomienda en PatagoniaWellboat
            try:
                reserva_encomienda.destinatario = self.destinatario
                reserva_encomienda.destino = self.destino
                reserva_encomienda.precio = precio_total
                reserva_encomienda.encomienda = encomienda_obj
                reserva_encomienda.fecha = date.today()
            except Exception:
                pass

            if self.patagonia_wellboat:
                self.patagonia_wellboat.agregar_reserva(reserva_encomienda)
                
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def volver_atras(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()