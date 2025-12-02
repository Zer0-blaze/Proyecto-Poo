from PyQt6.QtWidgets import QWidget, QPushButton

# Aun no esta implementado el panel de gerente, ya que, primero se debe implementar el verficador de login

class Gerente(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent_window = parent 
        self.destino_seleccionado = None
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Gerente Panel")
        self.setGeometry(400, 100, 900, 600)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

       # Botón Cerrar Sesión
        self.btn_cerrar_sesion = QPushButton("Cerrar Sesión", self)
        self.btn_cerrar_sesion.resize(120, 35)
        self.btn_cerrar_sesion.move(750, 20)
        self.btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)

        # Lógica del panel de gerente en proceso

    # Nueva función: cerrar sesión 
    def cerrar_sesion(self):
        if self.parent_window:
            self.parent_window.show()
            self.close()  