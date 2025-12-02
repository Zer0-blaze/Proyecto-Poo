from PyQt6.QtWidgets import QWidget, QPushButton



class DetallesUsuario(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent_window = parent 
        self.destino_seleccionado = None
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Patagonia Wellboat - Detalles Compra")
        self.setGeometry(400, 100, 900, 600)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

       # Botón Cancelar Compra
        self.btn_cerrar_compra = QPushButton("Cancelar Compra", self)
        self.btn_cerrar_compra.resize(120, 35)
        self.btn_cerrar_compra.move(750, 20)
        self.btn_cerrar_compra.clicked.connect(self.cerrar_compra)

        

    def cerrar_compra(self):
        if self.parent_window:
            self.parent_window.show()
            self.close() 