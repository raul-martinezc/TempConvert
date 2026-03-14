import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtGui import QDoubleValidator

class TempConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temperature Converter")

        layout = QVBoxLayout()

        self.celsius_label = QLabel("Celsius")
        self.celsius_input = QLineEdit()
        self.celsius_input.setValidator(QDoubleValidator(-1000, 1000, 2))
        self.celsius_input.textChanged.connect(self.update_fahrenheit)

        self.fahrenheit_label = QLabel("Fahrenheit")
        self.fahrenheit_input = QLineEdit()
        self.fahrenheit_input.setValidator(QDoubleValidator(-1000, 1000, 2))
        self.fahrenheit_input.textChanged.connect(self.update_celsius)

        layout.addWidget(self.celsius_label)
        layout.addWidget(self.celsius_input)
        layout.addWidget(self.fahrenheit_label)
        layout.addWidget(self.fahrenheit_input)

        self.setLayout(layout)

    def update_fahrenheit(self):
        try:
            celsius = float(self.celsius_input.text())
            self.fahrenheit_input.blockSignals(True)
            self.fahrenheit_input.setText(f"{celsius * 9 / 5 + 32:.2f}")
            self.fahrenheit_input.blockSignals(False)
        except ValueError:
            pass

    def update_celsius(self):
        try:
            fahrenheit = float(self.fahrenheit_input.text())
            self.celsius_input.blockSignals(True)
            self.celsius_input.setText(f"{(fahrenheit - 32) * 5 / 9:.2f}")
            self.celsius_input.blockSignals(False)
        except ValueError:
            pass

if __name__ == "__main__":
    app = QApplication([])

    window = TempConverter()
    window.resize(200, 100)
    window.show()

    sys.exit(app.exec())
