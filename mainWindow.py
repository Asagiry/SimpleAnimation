
from PySide6.QtCore import QAbstractAnimation, QEasingCurve, QParallelAnimationGroup, QPoint, QPropertyAnimation, QRect, QRectF, Qt
from PySide6.QtGui import QColor
from Square import SquareWidget
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene, QGridLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget
from ellipse import EllipseWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,600)
        
        self.duration = 500
        
        self.button = QPushButton(self)
        self.button.setGeometry(400,250,200,100)
        self.button.setText("Запустить анимацию")
        self.button.clicked.connect(self.clicked)
        
        self.squareblue = SquareWidget(self,Qt.blue)
        self.squareblue.setGeometry(0,0,200,200)
        
        self.squarered = SquareWidget(self,Qt.red)
        self.squarered.setGeometry(800,400,200,200)
        
        self.squaregreen = SquareWidget(self,Qt.green)
        self.squaregreen.setGeometry(0,400,200,200)
        
        self.squareyellow = SquareWidget(self,Qt.yellow)
        self.squareyellow.setGeometry(800,0,200,200)
        
        self.ellipse1 = EllipseWidget(self)
        self.ellipse1.setGeometry(200,175,80,80)
        
        self.ellipse2 = EllipseWidget(self)
        self.ellipse2.setGeometry(200,350,80,80)
        
    def clicked(self):
        self.right(self.squareblue)
        self.left(self.squarered)
        self.up(self.squaregreen)
        self.down(self.squareyellow)
        self.ParallelAnimation()
        
       
     
    def ParallelAnimation(self):
        
        anim1 = QPropertyAnimation(self.ellipse1, b"pos",self)
        anim1.setDuration(1000)  
        anim1.setStartValue(QPoint(200,175))  
        anim1.setEndValue(QPoint(725,175)) 
        anim1.setEasingCurve(QEasingCurve.OutInQuad)
        
        anim2 = QPropertyAnimation(self.ellipse2, b"pos",self)
        anim2.setDuration(1000) 
        anim2.setStartValue(QPoint(200,350)) 
        anim2.setEndValue(QPoint(725,350)) 
        anim2.setEasingCurve(QEasingCurve.OutInQuad)
        
        self.parallelAnim = QParallelAnimationGroup(self)
        self.parallelAnim.addAnimation(anim1)
        self.parallelAnim.addAnimation(anim2)
        self.parallelAnim.start()
        self.parallelAnim.finished.connect(lambda: (self.changeDirection(),self.parallelAnim.start()))
                                                                  
                                                                  
    def changeDirection(self):
        if self.parallelAnim.direction() == QAbstractAnimation.Forward:
            self.parallelAnim.setDirection(QAbstractAnimation.Backward)
        else:
            self.parallelAnim.setDirection(QAbstractAnimation.Forward)
      
        
    def right(self,square):
        anim = QPropertyAnimation(square, b"pos", self)
        anim.setDuration(self.duration)
        anim.setStartValue(QPoint(0, 0))
        anim.setEndValue(QPoint(800, 0))
        anim.setEasingCurve(QEasingCurve.InExpo)
        anim.start()
        anim.finished.connect(lambda: self.down(square))
        
    def down(self,square):
        anim = QPropertyAnimation(square, b"pos", self)
        anim.setDuration(self.duration)
        anim.setStartValue(QPoint(800, 0))
        anim.setEndValue(QPoint(800, 400))
        anim.setEasingCurve(QEasingCurve.InExpo)
        anim.start()
        anim.finished.connect(lambda: self.left(square))
        
    def left(self,square):
        anim = QPropertyAnimation(square, b"pos", self)
        anim.setDuration(self.duration)
        anim.setStartValue(QPoint(800, 400))
        anim.setEndValue(QPoint(0,400))
        anim.setEasingCurve(QEasingCurve.InExpo)
        anim.start()
        anim.finished.connect(lambda: self.up(square))
    def up(self,square):
        anim = QPropertyAnimation(square, b"pos", self)
        anim.setDuration(self.duration)
        anim.setStartValue(QPoint(0, 400))
        anim.setEndValue(QPoint(0,0))
        anim.setEasingCurve(QEasingCurve.InExpo)
        anim.start()
        anim.finished.connect(lambda: self.right(square))