from PySide6.QtWidgets import QApplication, QDialog
from test1 import Ui_Dialog

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones a funciones
        self.buttonBox.accepted.connect(self.ok_pressed)
        self.buttonBox.rejected.connect(self.cancel_pressed)
        self.pushButtonLove.clicked.connect(self.love_pressed)

    def ok_pressed(self):
        self.label.setText("¡Presionaste OK!")

    def cancel_pressed(self):
        self.label.setText("Cancelaste la acción.")

    def love_pressed(self):
        self.label.setText("ILY")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()