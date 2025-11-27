import sys
from PyQt6.QtWidgets import QApplication

from Interfaz.Principal import Principal


def main():
    app = QApplication(sys.argv)

    ventana = Principal()   
    ventana.show()        

    sys.exit(app.exec())


if __name__ == "__main__":
    main()