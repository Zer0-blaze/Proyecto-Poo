from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtGui import QFont
from Interfaz.VerClientes import VerClientes
from Interfaz.VerEncomiendas import VerEncomiendas

class Gerente(QWidget):
    def __init__(self, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.patagonia_wellboat = patagonia_wellboat
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Panel Gerente")
        self.setGeometry(400, 100, 1000, 700)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        # Botón Cerrar Sesión
        self.btn_cerrar_sesion = QPushButton("Cerrar Sesión", self)
        self.btn_cerrar_sesion.resize(120, 35)
        self.btn_cerrar_sesion.move(850, 20)
        self.btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)

        # Título
        titulo = QLabel("Panel de Administración", self)
        titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        titulo.move(50, 70)

        pos_y = 130
        espaciado = 60

        # Clientes
        self.btn_ver_clientes = QPushButton("Ver Clientes", self)
        self.btn_ver_clientes.resize(180, 40)
        self.btn_ver_clientes.move(50, pos_y)

        self.btn_ver_clientes.clicked.connect(self.ver_clientes)

        self.btn_editar_clientes = QPushButton("Editar Clientes", self)
        self.btn_editar_clientes.resize(180, 40)
        self.btn_editar_clientes.move(260, pos_y)
        self.btn_editar_clientes.clicked.connect(self.editar_clientes)

        # Ventas
        pos_y += espaciado
        self.btn_ver_ventas = QPushButton("Ver Ventas", self)
        self.btn_ver_ventas.resize(180, 40)
        self.btn_ver_ventas.move(50, pos_y)

        self.btn_ver_ventas.clicked.connect(self.ver_ventas)

        self.btn_editar_ventas = QPushButton("Editar Ventas", self)
        self.btn_editar_ventas.resize(180, 40)
        self.btn_editar_ventas.move(260, pos_y)
        self.btn_editar_ventas.clicked.connect(self.editar_ventas)

        # Reservas
        pos_y += espaciado
        self.btn_ver_reservas = QPushButton("Ver Reservas", self)
        self.btn_ver_reservas.resize(180, 40)
        self.btn_ver_reservas.move(50, pos_y)

        self.btn_ver_reservas.clicked.connect(self.ver_reservas)

        self.btn_editar_reservas = QPushButton("Editar Reservas", self)
        self.btn_editar_reservas.resize(180, 40)
        self.btn_editar_reservas.move(260, pos_y)
        self.btn_editar_reservas.clicked.connect(self.editar_reservas)

        # Encomiendas
        pos_y += espaciado
        self.btn_ver_encomiendas = QPushButton("Ver Encomiendas", self)
        self.btn_ver_encomiendas.resize(180, 40)
        self.btn_ver_encomiendas.move(50, pos_y)

        self.btn_ver_encomiendas.clicked.connect(self.ver_encomiendas)

        self.btn_editar_encomiendas = QPushButton("Editar Encomiendas", self)
        self.btn_editar_encomiendas.resize(180, 40)
        self.btn_editar_encomiendas.move(260, pos_y)
        self.btn_editar_encomiendas.clicked.connect(self.editar_encomiendas)

    # Metodos para ver información
    def ver_clientes(self):
        self.ventana_clientes = VerClientes(self.patagonia_wellboat, self)
        self.hide()

    def ver_ventas(self):
        from Interfaz.VerVentas import VerVentas
        self.ventana_ventas = VerVentas(self.patagonia_wellboat, self)
        self.hide()

    def ver_reservas(self):
        from Interfaz.VerReservas import VerReservas
        self.ventana_reservas = VerReservas(self.patagonia_wellboat, self)
        self.hide()

    def ver_encomiendas(self):
        
        self.ventana_encomiendas = VerEncomiendas(self.patagonia_wellboat, self)
        self.hide()

    # === MÉTODOS PARA EDITAR INFORMACIÓN ===
    def editar_clientes(self):
        # TODO: Abrir ventana para editar clientes
        print("Editar clientes - En desarrollo")

    def editar_ventas(self):
        # TODO: Abrir ventana para editar ventas
        print("Editar ventas - En desarrollo")

    def editar_reservas(self):
        # TODO: Abrir ventana para editar reservas
        print("Editar reservas - En desarrollo")

    def editar_encomiendas(self):
        # TODO: Abrir ventana para editar encomiendas
        print("Editar encomiendas - En desarrollo")

    def cerrar_sesion(self):
        if self.parent_window:
            self.parent_window.show()
            self.close()  