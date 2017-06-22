import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class Crosshair(QtWidgets):
    #----------------------------------------------------------------------
    def __init__(self):
        super(Crosshair, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        
        
        self.initUI()
        """"""
        
    def initUI(self):
        self.setGeometry(0, 0, 2560, 1440)
        self.setWindowTitle('Crosshair Overlay')
        self.show()
        
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
        
    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, .5, QtCore.Qt.SolidLine)
        
        qp.setPen(pen)
        qp.drawLine(1280, 0, 1280, 1440)
        qp.drawLine(0, 720, 2560, 720)
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    crosshair = Crosshair()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
        