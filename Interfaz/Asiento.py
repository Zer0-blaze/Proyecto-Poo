from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel, QGridLayout, QMessageBox, QScrollArea
)
from PyQt6.QtGui import QFont
from Interfaz.DetallesUsuario import DetallesUsuario


class Asiento(QWidget):
    def __init__(self, embarcacion, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.embarcacion = embarcacion 
        self.patagonia_wellboat = patagonia_wellboat
        self.parent_window = parent

        self.asientos_seleccionados = []     

        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle(
            f"Patagonia Wellboat - Selección de Asiento ({self.embarcacion.nombre})"
        )
        self.setGeometry(400, 100, 900, 600)
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
      
        titulo = QLabel(f"Asientos disponibles para {self.embarcacion.nombre}", self)
        titulo.setFont(QFont("Arial", 16))
        titulo.move(20, 20)

        info_label = QLabel("Haz clic en los asientos para seleccionar múltiples asientos", self)
        info_label.setFont(QFont("Arial", 10))
        info_label.move(20, 50)

        # botón Volver
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.resize(80, 30)
        self.btn_volver.move(800, 20)
        self.btn_volver.clicked.connect(self.volver_atras)

        # Generar la cuadrícula de asientos
        self.layout = QGridLayout()
        total_asientos = int(getattr(self.embarcacion, 'capacidadPasajeros', 20))
        if total_asientos <= 20:
            columnas = 4
            h_spacing = 14
            v_spacing = 14
            button_w, button_h = 80, 44
        elif total_asientos <= 50:
            columnas = 5
            h_spacing = 14
            v_spacing = 16
            button_w, button_h = 82, 46
        else:
            columnas = 6
            h_spacing = 18
            v_spacing = 18
            button_w, button_h = 86, 48
        self.layout.setHorizontalSpacing(h_spacing)
        self.layout.setVerticalSpacing(v_spacing)
        self.botones_asientos = []

        fila = 0
        columna = 0
        for asiento_num in range(1, total_asientos + 1):

            boton = QPushButton(str(asiento_num))
            boton.setFixedSize(button_w, button_h)
            boton.clicked.connect(
                lambda checked, a=asiento_num: self.seleccionar_asiento(a)
            )

            self.layout.addWidget(boton, fila, columna)
            self.botones_asientos.append(boton)

            columna += 1
            if columna >= columnas:
                columna = 0
                fila += 1
        content_widget = QWidget()
        content_widget.setLayout(self.layout)

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setWidget(content_widget)
        cont_x = 40
        cont_y = 80
        cont_w = 820
        cont_h = 380
        scroll.setGeometry(cont_x, cont_y, cont_w, cont_h)

        # botón confirmar selección
        self.btn_confirmar = QPushButton("Confirmar Selección", self)
        self.btn_confirmar.resize(160, 44)
        confirm_x = int((self.width() - 160) / 2)
        confirm_y = cont_y + cont_h + 12
        self.btn_confirmar.move(confirm_x, confirm_y)
        self.btn_confirmar.clicked.connect(self.confirmar_asientos)

    #Input: Selección de asientos
    #Selecciona o deselecciona un asiento
    #Output: Actualiza la lista de asientos seleccionados y el estilo del botón
    def seleccionar_asiento(self, numero):
        if numero in self.asientos_seleccionados:
            self.asientos_seleccionados.remove(numero)
            self.botones_asientos[numero - 1].setStyleSheet("")
        else:
            self.asientos_seleccionados.append(numero)
            self.botones_asientos[numero - 1].setStyleSheet(
                "background-color: lightgreen; font-weight: bold;"
            )


    def confirmar_asientos(self):
        if not self.asientos_seleccionados:
            QMessageBox.warning(self, "Error", "Debes seleccionar al menos un asiento")
            return

        asientos_str = ", ".join(map(str, sorted(self.asientos_seleccionados)))
        QMessageBox.information(
            self, "Asientos Confirmados",
            f"Asientos seleccionados: {asientos_str}"
        )
        self.ventana_detalles = DetallesUsuario(parent=self.parent_window)
        self.ventana_detalles.show()
        self.close()

    def volver_atras(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()
