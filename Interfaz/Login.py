from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QLabel, QCheckBox, QMessageBox
)
from PyQt6.QtGui import QFont
from Interfaz.Gerente import Gerente


class Login(QWidget):
    def __init__(self, parent=None, patagonia_wellboat=None):
        super().__init__()
        self.patagonia_wellboat = patagonia_wellboat
        self.parent_window = parent
        self.destino_seleccionado = None
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Login Gerente")
        self.setGeometry(400, 100, 900, 600)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        # Botón Volver
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.resize(80, 30)
        self.btn_volver.move(800, 20)
        self.btn_volver.clicked.connect(self.volver_atras)

        # Nombre del gerente
        label_nombre = QLabel("Nombre:", self)
        label_nombre.setFont(QFont("Arial", 12))
        label_nombre.move(50, 80)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 35)
        self.user_input.move(250, 77)

        # Contraseña
        label_password = QLabel("Contraseña:", self)
        label_password.setFont(QFont("Arial", 12))
        label_password.move(50, 140)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 35)
        self.password_input.move(250, 137)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Mostrar/Ocultar contraseña
        self.check_ver_password = QCheckBox(self)
        self.check_ver_password.setText("Mostrar Contraseña")
        self.check_ver_password.move(250, 180)
        self.check_ver_password.clicked.connect(self.MostrarPassword)

        login_button = QPushButton("Iniciar Sesión", self)
        login_button.resize(150, 40)
        login_button.move(250, 220)
        login_button.clicked.connect(self.verificar)

    # Mostrar u ocultar contraseña
    def MostrarPassword(self, clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    # Verificar credenciales de gerente
    def verificar(self):
        nombre = self.user_input.text().strip()
        password = self.password_input.text().strip()
        gerente = self.patagonia_wellboat.gerentes
        if nombre != gerente.nombre:
            QMessageBox.warning(self, "Error", "nombre incorrecto")
            return
        if password != gerente.password:
            QMessageBox.warning(self, "Error", "contraseña incorrecta")
            return
        self.abrir_menu_gerente()

    def abrir_menu_gerente(self):
        parent_for_gerente = self.parent_window if self.parent_window is not None else self
        self.ventana_gerente = Gerente(parent=parent_for_gerente)
        self.ventana_gerente.show()
        self.close()

    def volver_atras(self):
        if self.parent_window:
            self.parent_window.show()
            self.close()