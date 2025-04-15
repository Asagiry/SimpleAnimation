from mainWindow import MainWindow
from PySide6.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget


app = QApplication()
window = MainWindow()
window.show()
app.exec()
