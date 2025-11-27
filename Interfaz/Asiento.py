from PyQt6.QtWidgets import QWidget, QPushButton
class Asiento(QWidget):
    def __init__(self, patagonia_wellboat, parent=None):
        super().__init__()
        self.patagonia_wellboat = patagonia_wellboat
        self.parent_window = parent 
        self.destino_seleccionado = None
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Reservar Viaje")
        self.setGeometry(400, 100, 900, 600)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        # Botón Volver
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.resize(80, 30)
        self.btn_volver.move(800, 20)
        self.btn_volver.clicked.connect(self.volver_atras)

    def volver_atras(self):
        if self.parent_window:
            self.parent_window.show()
            self.close()