from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont

class VerClientes(QWidget):
    def __init__(self, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.patagonia_wellboat = patagonia_wellboat
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Ver Clientes - Patagonia Wellboat")
        self.setGeometry(300, 100, 1000, 600)
        self.generar_formulario()
        self.cargar_clientes()
        self.show()

    def generar_formulario(self):

        # Botón Cerrar
        self.btn_cerrar = QPushButton("Cerrar", self)
        self.btn_cerrar.resize(100, 35)
        self.btn_cerrar.move(850, 540)
        self.btn_cerrar.clicked.connect(self.cerrar_ventana)

        # Título
        titulo = QLabel("Lista de Clientes Registrados", self)
        titulo.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        titulo.move(50, 20)

        # Tabla de clientes
        self.tabla_clientes = QTableWidget(self)
        self.tabla_clientes.setColumnCount(5)
        self.tabla_clientes.setHorizontalHeaderLabels(["Nombre", "RUT", "Historial de Viajes", "Contacto Emergencia", "Viajes Completados"])
        self.tabla_clientes.resize(900, 450)
        self.tabla_clientes.move(50, 70)
        self.tabla_clientes.setColumnWidth(0, 200)
        self.tabla_clientes.setColumnWidth(1, 150)
        self.tabla_clientes.setColumnWidth(2, 150)
        self.tabla_clientes.setColumnWidth(3, 200)
        self.tabla_clientes.setColumnWidth(4, 150)

    def cargar_clientes(self):
        if not self.patagonia_wellboat:
            return
        
        clientes = self.patagonia_wellboat.obtener_clientes()
        self.tabla_clientes.setRowCount(len(clientes))
        
        for fila, cliente in enumerate(clientes):
            # Nombre
            item_nombre = QTableWidgetItem(cliente.nombre)
            self.tabla_clientes.setItem(fila, 0, item_nombre)
            
            # RUT
            item_rut = QTableWidgetItem(cliente.rut)
            self.tabla_clientes.setItem(fila, 1, item_rut)
            
            # Historial de viajes (cantidad)
            item_historial = QTableWidgetItem(str(cliente.historial_viajes))
            self.tabla_clientes.setItem(fila, 2, item_historial)
            
            # Contacto de emergencia
            item_emergencia = QTableWidgetItem(cliente.emergencia)
            self.tabla_clientes.setItem(fila, 3, item_emergencia)
            
            # Viajes completados
            item_viajes = QTableWidgetItem(str(cliente.historial_viajes))
            self.tabla_clientes.setItem(fila, 4, item_viajes)

    def cerrar_ventana(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()
