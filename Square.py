from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QPainter, QPainterPath, QPolygon
from PySide6.QtWidgets import QWidget

class SquareWidget(QWidget):
    def __init__(self,parent,color):
        super().__init__(parent)
        self.color = color
        
    def paintEvent(self, event):
       
        painter = QPainter(self)
        self.Length = 200
        square = QPainterPath()
        square.moveTo(0,0)
        square.lineTo(0,self.Length)
        square.lineTo(self.Length,self.Length)
        square.lineTo(self.Length,0)
        square.lineTo(0,0)
        painter.fillPath(square,self.color)