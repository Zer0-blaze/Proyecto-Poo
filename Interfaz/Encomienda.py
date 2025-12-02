from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QPushButton, QLabel, QMenu, QMessageBox
)
from PyQt6.QtGui import QFont
from functools import partial
from Modelo.destino import DESTINOS, Destino
from Modelo.encomienda import encomienda


class Encomienda(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent_window = parent
        self.destino_seleccionado = None
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Enviar Encomienda")
        self.setGeometry(400, 100, 900, 600)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        # Botón Volver
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.resize(80, 30)
        self.btn_volver.move(800, 20)
        self.btn_volver.clicked.connect(self.volver_atras)

        # Remitente
        label_remitente = QLabel("Remitente:", self)
        label_remitente.setFont(QFont("Arial", 12))
        label_remitente.move(50, 80)

        self.input_remitente = QLineEdit(self)
        self.input_remitente.resize(250, 35)
        self.input_remitente.move(250, 77)

        # Destinatario
        label_destinatario = QLabel("Destinatario:", self)
        label_destinatario.setFont(QFont("Arial", 12))
        label_destinatario.move(50, 140)

        self.input_destinatario = QLineEdit(self)
        self.input_destinatario.resize(250, 35)
        self.input_destinatario.move(250, 137)

        # Destino
        self.btn_destinos = QPushButton("Seleccionar destino", self)
        self.btn_destinos.resize(250, 40)
        self.btn_destinos.move(250, 200)

        self.label_precio = QLabel("Precio: -", self)
        self.label_precio.setFont(QFont("Arial", 12))
        self.label_precio.resize(250, 30)
        self.label_precio.move(250, 245)

        menu = QMenu()
        for destino in DESTINOS:
            action = menu.addAction(destino.nombre)
            action.triggered.connect(partial(self.seleccionar_destino, destino))

        self.btn_destinos.setMenu(menu)

        # Peso
        label_peso = QLabel("Peso (kg):", self)
        label_peso.setFont(QFont("Arial", 12))
        label_peso.move(50, 300)

        self.input_peso = QLineEdit(self)
        self.input_peso.resize(250, 35)
        self.input_peso.move(250, 297)

        # Botón enviar
        self.btn_enviar = QPushButton("Confirmar Encomienda", self)
        self.btn_enviar.resize(250, 40)
        self.btn_enviar.move(250, 360)
        self.btn_enviar.clicked.connect(self.enviar_encomienda)

    # Selecciona el destino y actualiza el botón y la etiqueta de precio
    def seleccionar_destino(self, destino: Destino):
        self.destino_seleccionado = destino
        self.btn_destinos.setText(destino.nombre)
        self.label_precio.setText(f"Precio: ${destino.precio_encomienda} por kg")

    #Se encarga de enviar la encomienda después de verificar los campos
    def enviar_encomienda(self):
        if not self.input_remitente.text() or not self.input_destinatario.text():
            QMessageBox.warning(self, "Error", "Debe completar todos los campos antes.")
            return
        if not self.destino_seleccionado:
            QMessageBox.warning(self, "Error", "Debe seleccionar un destino antes.")
            return

        remitente = self.input_remitente.text()
        destinatario = self.input_destinatario.text()
        try:
            peso = float(self.input_peso.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Peso inválido.")
            return
        
    # Legendaria función para el botón volver
    def volver_atras(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()