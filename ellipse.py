


import math
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QLinearGradient, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget


class EllipseWidget(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
   
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Для плавного рендеринга

        pen = painter.pen()
        pen.setColor(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        
        gradient = QLinearGradient(0, 0, 200, 200) 
        gradient.setColorAt(0, QColor(81, 0, 135))
        gradient.setColorAt(0.5, QColor(241, 91, 132))
        gradient.setColorAt(1, QColor(155, 79, 165))
    
        brush = QBrush(gradient)
        
        painter.setBrush(brush)
        
        self.diam = 75
        painter.drawEllipse(1, 1, self.diam, self.diam)