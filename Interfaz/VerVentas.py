from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont
from datetime import datetime, date
from Modelo.reserva import ReservaPasaje as RPas, ReservaEncomienda as REnc

class VerVentas(QWidget):
    def __init__(self, patagonia_wellboat=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.patagonia_wellboat = patagonia_wellboat
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Ver Ventas - Patagonia Wellboat")
        self.setGeometry(300, 100, 1000, 600)
        self.generar_formulario()
        self.cargar_ventas()
        self.show()

    def generar_formulario(self):
        # Título
        titulo = QLabel("Registro de Ventas", self)
        titulo.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        titulo.move(50, 20)

        # Tabla de ventas
        self.tabla_ventas = QTableWidget(self)
        self.tabla_ventas.setColumnCount(6)
        self.tabla_ventas.setHorizontalHeaderLabels(["ID Venta", "Cliente", "Monto Pagado", "Fecha", "Tipo (Pasaje/Encomienda)", "Viaje/Destino"])
        self.tabla_ventas.resize(900, 450)
        self.tabla_ventas.move(50, 70)
        self.tabla_ventas.setColumnWidth(0, 100)
        self.tabla_ventas.setColumnWidth(1, 180)
        self.tabla_ventas.setColumnWidth(2, 130)
        self.tabla_ventas.setColumnWidth(3, 120)
        self.tabla_ventas.setColumnWidth(4, 170)
        self.tabla_ventas.setColumnWidth(5, 150)

        # Botón Cerrar
        self.btn_cerrar = QPushButton("Cerrar", self)
        self.btn_cerrar.resize(100, 35)
        self.btn_cerrar.move(850, 540)
        self.btn_cerrar.clicked.connect(self.cerrar_ventana)

    def cargar_ventas(self):
        if not self.patagonia_wellboat:
            return
        
        ventas = self.patagonia_wellboat.obtener_ventas() or []
        reservas_all = self.patagonia_wellboat.obtener_reservas() or []
        self.tabla_ventas.setRowCount(len(ventas))

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
                    return fecha_val

        for fila, venta in enumerate(ventas):
            # ID Venta
            item_id = QTableWidgetItem(str(venta.id))
            self.tabla_ventas.setItem(fila, 0, item_id)
            
            # Cliente
            cliente_nombre = venta.cliente.nombre if venta.cliente else "N/A"
            item_cliente = QTableWidgetItem(cliente_nombre)
            self.tabla_ventas.setItem(fila, 1, item_cliente)
            
            # Monto Pagado
            monto_val = venta.total_paga
            try:
                monto_str = f"${int(monto_val):,}" if float(monto_val).is_integer() else f"${monto_val}"
            except Exception:
                monto_str = f"${monto_val}"
            item_monto = QTableWidgetItem(monto_str)
            self.tabla_ventas.setItem(fila, 2, item_monto)

            # Fecha
            item_fecha = QTableWidgetItem(format_fecha(getattr(venta, 'fecha', None)))
            self.tabla_ventas.setItem(fila, 3, item_fecha)

            # Determinar tipo buscando reservas relacionadas a esta venta
            related = [r for r in reservas_all if getattr(r, 'id', None) == getattr(venta, 'id', None) or getattr(r, 'cliente', None) is getattr(venta, 'cliente', None)]
            if not related:
                v_name = getattr(venta, 'cliente', None)
                v_name = v_name.nombre.lower() if v_name and hasattr(v_name, 'nombre') else None
                if v_name:
                    related = [r for r in reservas_all if getattr(r, 'cliente', None) and hasattr(r.cliente, 'nombre') and r.cliente.nombre.lower() == v_name]
            tipo = "Desconocido"
            destino_info = "-"
            if related:
                if any(isinstance(r, RPas) for r in related):
                    tipo = "Pasaje"
                    rp = next((r for r in related if isinstance(r, RPas)), None)
                    if rp:
                        destino_obj = getattr(rp, 'destino', None)
                        if destino_obj and hasattr(destino_obj, 'nombre'):
                            destino_info = destino_obj.nombre
                        else:
                            destino_info = getattr(rp, 'destino', str(destino_obj)) if destino_obj else "-"
                elif any(isinstance(r, REnc) for r in related):
                    tipo = "Encomienda"
                    ren = next((r for r in related if isinstance(r, REnc)), None)
                    if ren:
                        destino_obj = getattr(ren, 'destino', None)
                        if destino_obj and hasattr(destino_obj, 'nombre'):
                            destino_info = destino_obj.nombre
                        else:
                            destino_info = getattr(ren, 'destino', str(destino_obj)) if destino_obj else "-"
            else:
                tipo = "Pasaje" if getattr(venta, 'viaje', None) else "Encomienda"
                try:
                    destino_info = venta.viaje.destino.nombre if getattr(venta, 'viaje', None) and getattr(venta.viaje, 'destino', None) else (venta.viaje if getattr(venta, 'viaje', None) else "Encomienda")
                except Exception:
                    destino_info = "Encomienda"

            item_tipo = QTableWidgetItem(tipo)
            self.tabla_ventas.setItem(fila, 4, item_tipo)

            item_destino = QTableWidgetItem(str(destino_info))
            self.tabla_ventas.setItem(fila, 5, item_destino)

    def cerrar_ventana(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()
