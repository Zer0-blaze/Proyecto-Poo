from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QPushButton, QLabel, QMenu, QMessageBox, QDateEdit
)
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QFont
from functools import partial
from Interfaz.Asiento import Asiento
from Modelo.destino import DESTINOS, Destino
from Modelo.embarcacion import CatamaranLiviano, FerryMediano, WellboatGranCapacidad

class Usuario(QWidget):
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

        # Nombre 
        label_nombre = QLabel("Nombre Completo:", self)
        label_nombre.setFont(QFont("Arial", 12))
        label_nombre.move(50, 80)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 35)
        self.user_input.move(250, 77)

        # RUT 
        label_rut = QLabel("RUT:", self)
        label_rut.setFont(QFont("Arial", 12))
        label_rut.move(50, 140)

        self.rut_input = QLineEdit(self)
        self.rut_input.resize(250, 35)
        self.rut_input.move(250, 137)

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

        # Fecha del viaje
        label_fecha = QLabel("Fecha del viaje:", self)
        label_fecha.setFont(QFont("Arial", 12))
        label_fecha.move(50, 290)

        self.selector_fecha = QDateEdit(self)
        self.selector_fecha.setCalendarPopup(True)
        self.selector_fecha.setDate(QDate.currentDate())
        self.selector_fecha.move(250, 287)
        self.selector_fecha.resize(250, 35)

        # Embarcación
        self.btn_embarcaciones = QPushButton("Seleccionar embarcación", self)
        self.btn_embarcaciones.resize(250, 40)
        self.btn_embarcaciones.move(250, 335)
        self._embarcaciones_disponibles = [CatamaranLiviano(), FerryMediano(), WellboatGranCapacidad()]
        menu_emb = QMenu()
        for barco in self._embarcaciones_disponibles:
            act = menu_emb.addAction(barco.nombre)
            act.triggered.connect(partial(self.seleccionar_embarcacion, barco))
        self.btn_embarcaciones.setMenu(menu_emb)
        self.embarcacion_seleccionada = None

        # Botón seleccionar asiento
        self.btn_asiento = QPushButton("Seleccionar Asiento", self)
        self.btn_asiento.resize(250, 40)
        self.btn_asiento.move(250, 420)
        self.btn_asiento.clicked.connect(self.abrir_ventana_asiento)

    def seleccionar_destino(self, destino: Destino):
        self.destino_seleccionado = destino
        self.btn_destinos.setText(destino.nombre)
        self.label_precio.setText(f"Precio: ${destino.precio_pasaje}  X persona")

    # Abrir ventana de selección de asiento tras validar campos obligatorios
    def abrir_ventana_asiento(self):

        if not self.user_input.text() or not self.rut_input.text():
            QMessageBox.warning(self, "Error", "Debe completar todos los campos antes.")
            return

        if not self.destino_seleccionado:
            QMessageBox.warning(self, "Error", "Debe seleccionar un destino antes.")
            return

        if not self.embarcacion_seleccionada:
            QMessageBox.warning(self, "Error", "Debe seleccionar una embarcación antes.")
            return

        nombre = self.user_input.text()
        rut = self.rut_input.text()

        self.ventana_asiento = Asiento(
            self.embarcacion_seleccionada, 
            self.patagonia_wellboat, 
            parent=self,
            destino=self.destino_seleccionado,
            nombre_cliente=nombre,
            rut_cliente=rut,
            fecha_viaje=self.selector_fecha.date().toString("dd/MM/yyyy")
        )
        self.ventana_asiento.show()
        self.hide()
        
    # Retrocede a la ventana anterior
    def volver_atras(self):
        if self.parent_window:
            self.parent_window.show()   
        self.close()

    # Selecciona la embarcación
    def seleccionar_embarcacion(self, embarcacion: object):
        self.embarcacion_seleccionada = embarcacion
        try:
            self.btn_embarcaciones.setText(embarcacion.nombre)
        except Exception:
            pass
