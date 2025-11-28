from PyQt6.QtWidgets import QWidget, QPushButton
from Interfaz.Usuario import Usuario
from Interfaz.Encomienda import Encomienda
from Interfaz.Login import Login
from Modelo.PatagoniaWellboat import PatagoniaWellboat

class Principal(QWidget):
    def __init__(self):
        super().__init__()
        self.patagonia_wellboat = PatagoniaWellboat()
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Principal")
        self.setGeometry(400, 100, 900, 600)

        self.btn_agendar = QPushButton("Agendar Viaje", self)
        self.btn_agendar.resize(200, 40)
        self.btn_agendar.move(50, 100)
        self.btn_agendar.clicked.connect(self.abrir_ventana_usuario)

        self.btn_encomienda = QPushButton("Enviar Encomiendas", self)
        self.btn_encomienda.resize(200, 40)
        self.btn_encomienda.move(50, 160)
        self.btn_encomienda.clicked.connect(self.abrir_ventana_encomienda)

        self.btn_gerente = QPushButton("Gerente", self)
        self.btn_gerente.resize(200, 40)
        self.btn_gerente.move(50, 220)
        self.btn_gerente.clicked.connect(self.abrir_ventana_gerente)

    def abrir_ventana_usuario(self):
        self.ventana_usuario = Usuario(self.patagonia_wellboat, parent=self)
        self.ventana_usuario.show()
        self.hide()

    def abrir_ventana_encomienda(self):
        self.ventana_encomienda = Encomienda(parent=self)
        self.ventana_encomienda.show()
        self.hide()
    
    def abrir_ventana_gerente(self):
        self.ventana_gerente = Login(parent=self)
        self.ventana_gerente.show()
        self.hide()