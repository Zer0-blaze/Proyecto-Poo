from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont
from Modelo.reserva import ReservaPasaje, ReservaEncomienda
from datetime import datetime, date

class VerReservas(QWidget):
    def __init__(self, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.patagonia_wellboat = patagonia_wellboat
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Ver Reservas - Patagonia Wellboat")
        self.setGeometry(300, 100, 1200, 600)
        self.generar_formulario()
        try:
            self.cargar_reservas()
        except Exception as e:
            print("[VerReservas] Error al cargar reservas:", e)
        self.show()

    def generar_formulario(self):
        # Título
        titulo = QLabel("Registro de Reservas", self)
        titulo.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        titulo.move(50, 20)

        # Tabla de reservas
        self.tabla_reservas = QTableWidget(self)
        self.tabla_reservas.setColumnCount(6)
        self.tabla_reservas.setHorizontalHeaderLabels(["ID Reserva", "Cliente", "Tipo", "Detalle", "Fecha", "Estado"])
        self.tabla_reservas.resize(1100, 450)
        self.tabla_reservas.move(50, 70)
        self.tabla_reservas.setColumnWidth(0, 120)
        self.tabla_reservas.setColumnWidth(1, 180)
        self.tabla_reservas.setColumnWidth(2, 120)
        self.tabla_reservas.setColumnWidth(3, 350)
        self.tabla_reservas.setColumnWidth(4, 150)
        self.tabla_reservas.setColumnWidth(5, 100)

        # Botón Cerrar
        self.btn_cerrar = QPushButton("Cerrar", self)
        self.btn_cerrar.resize(100, 35)
        self.btn_cerrar.move(1050, 540)
        self.btn_cerrar.clicked.connect(self.cerrar_ventana)

    def cargar_reservas(self):
        try:
            if not self.patagonia_wellboat:
                return
            
            reservas_raw = self.patagonia_wellboat.obtener_reservas() or []
            # Filtrar sólo objetos de tipo ReservaPasaje o ReservaEncomienda
            reservas = [r for r in reservas_raw if isinstance(r, (ReservaPasaje, ReservaEncomienda))]
            self.tabla_reservas.setRowCount(len(reservas))

            def format_fecha(fecha_val):
                if not fecha_val:
                    return "-"
                if isinstance(fecha_val, (datetime, date)):
                    try:
                        return fecha_val.strftime("%d/%m/%Y")
                    except Exception:
                        return str(fecha_val)
                if isinstance(fecha_val, str):
                    try:
                        dt = datetime.strptime(fecha_val, "%Y-%m-%d")
                        return dt.strftime("%d/%m/%Y")
                    except Exception:
                        try:
                            dt = datetime.strptime(fecha_val, "%d/%m/%Y")
                            return dt.strftime("%d/%m/%Y")
                        except Exception:
                            return fecha_val

            for fila, reserva in enumerate(reservas):
                try:
                    # ID Reserva
                    id_val = getattr(reserva, 'id', None)
                    if not id_val:
                        id_val = f"RES-{fila+1:04d}"
                    item_id = QTableWidgetItem(str(id_val))
                    self.tabla_reservas.setItem(fila, 0, item_id)
                except Exception as e:
                    print(f"[VerReservas] Error en ID fila {fila}: {e}")
                    self.tabla_reservas.setItem(fila, 0, QTableWidgetItem(f"RES-{fila+1:04d}"))
                
                try:
                    # Cliente
                    cliente = getattr(reserva, 'cliente', None)
                    cliente_nombre = cliente.nombre if cliente and hasattr(cliente, 'nombre') else "N/A"
                    item_cliente = QTableWidgetItem(cliente_nombre)
                    self.tabla_reservas.setItem(fila, 1, item_cliente)
                except Exception as e:
                    print(f"[VerReservas] Error en cliente fila {fila}: {e}")
                    self.tabla_reservas.setItem(fila, 1, QTableWidgetItem("N/A"))
                
                try:
                    # Tipo de reserva (Pasaje o Encomienda)
                    if isinstance(reserva, ReservaPasaje):
                        tipo = "Pasaje"
                        # Intentar obtener lista de asientos primero, luego asiento individual
                        asientos_lista = getattr(reserva, 'asientos_lista', None)
                        if asientos_lista:
                            asientos_str = ", ".join(map(str, asientos_lista))
                            detalle = f"Asientos: {asientos_str}"
                        else:
                            asiento_val = getattr(reserva, 'asiento', None)
                            if asiento_val and hasattr(asiento_val, 'numero'):
                                detalle = f"Asiento: {asiento_val.numero}"
                            else:
                                detalle = f"Asiento: {asiento_val}"
                    elif isinstance(reserva, ReservaEncomienda):
                        tipo = "Encomienda"
                        peso = getattr(reserva, 'peso', getattr(reserva, 'pesoKg', 'N/A'))
                        detalle = f"Peso: {peso} kg"
                    else:
                        tipo = "Desconocido"
                        detalle = "-"
                    
                    item_tipo = QTableWidgetItem(tipo)
                    self.tabla_reservas.setItem(fila, 2, item_tipo)
                    
                    # Detalle
                    item_detalle = QTableWidgetItem(detalle)
                    self.tabla_reservas.setItem(fila, 3, item_detalle)
                except Exception as e:
                    print(f"[VerReservas] Error en tipo/detalle fila {fila}: {e}")
                    self.tabla_reservas.setItem(fila, 2, QTableWidgetItem("Desconocido"))
                    self.tabla_reservas.setItem(fila, 3, QTableWidgetItem("-"))
                
                try:
                    # Fecha (si está disponible)
                    fecha_val = getattr(reserva, 'fecha', None)
                    fecha = format_fecha(fecha_val)
                    item_fecha = QTableWidgetItem(fecha)
                    self.tabla_reservas.setItem(fila, 4, item_fecha)
                except Exception as e:
                    print(f"[VerReservas] Error en fecha fila {fila}: {e}")
                    self.tabla_reservas.setItem(fila, 4, QTableWidgetItem("-"))
                
                try:
                    # Estado (por defecto "Activa")
                    estado = "Activa"
                    item_estado = QTableWidgetItem(estado)
                    self.tabla_reservas.setItem(fila, 5, item_estado)
                except Exception as e:
                    print(f"[VerReservas] Error en estado fila {fila}: {e}")
                    self.tabla_reservas.setItem(fila, 5, QTableWidgetItem("Activa"))
        except Exception as e:
            print("[VerReservas] Error general al cargar reservas:", e)

    def cerrar_ventana(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()
