from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        titulo = "TCC Teste"
        topo = 60
        esquerda = 40
        largura = 1200
        altura = 670

        icone = "icons/icone.png"

        self.setWindowTitle(titulo)
        self.setGeometry(topo, esquerda, largura, altura)
        self.setWindowIcon(QIcon(icone))

        self.image
Process finished with exit code 1
= QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brush_size = 1
        self.brush_color = Qt.black
        self.lastPoint = QPoint()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("Arquivo")
        brush_size = main_menu.addMenu("Tamanho")
        brush_color = main_menu.addMenu("Cor")

        save_action = QAction(QIcon("icons/salvar.png"), "Salvar", self)
        save_action.setShortcut("Ctrl+S")
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save)

        clear_action = QAction(QIcon("icons/limpar.png"), "Limpar", self)
        clear_action.setShortcut("Ctrl+C")
        file_menu.addAction(clear_action)
        clear_action.triggered.connect(self.clear)

        onepx_action = QAction(QIcon("icons/pixelum.png"), "1px", self)
        brush_size.addAction(onepx_action)
        onepx_action.triggered.connect(self.onePixel)

        threepx_action = QAction(QIcon("icons/pixeltres.png"), "3px", self)
        brush_size.addAction(threepx_action)
        threepx_action.triggered.connect(self.threePixel)

        fivepx_action = QAction(QIcon("icons/pixelcinco.png"), "5px", self)
        brush_size.addAction(fivepx_action)
        fivepx_action.triggered.connect(self.fivePixel)

        sevenpx_action = QAction(QIcon("icons/pixelsete.png"), "7px", self)
        brush_size.addAction(sevenpx_action)
        sevenpx_action.triggered.connect(self.sevenPixel)

        ninepx_action = QAction(QIcon("icons/pixelnove.png"), "9px", self)
        brush_size.addAction(ninepx_action)
        ninepx_action.triggered.connect(self.ninePixel)

        black_action = QAction(QIcon("icons/preto.png"), "Preto", self)
        black_action.setShortcut("Ctrl+Q")
        brush_color.addAction(black_action)
        black_action.triggered.connect(self.blackColor)

        bluek_action = QAction(QIcon("icons/azul.png"), "Azul", self)
        bluek_action.setShortcut("Ctrl+W")
        brush_color.addAction(bluek_action)
        bluek_action.triggered.connect(self.blueColor)

        red_action = QAction(QIcon("icons/vermelho.png"), "Vermelho", self)
        red_action.setShortcut("Ctrl+E")
        brush_color.addAction(red_action)
        red_action.triggered.connect(self.redColor)

        green_action = QAction(QIcon("icons/verde.png"), "Verde", self)
        green_action.setShortcut("Ctrl+R")
        brush_color.addAction(green_action)
        green_action.triggered.connect(self.greenColor)

        yellow_action = QAction(QIcon("icons/amarelo.png"), "Amarelo", self)
        yellow_action.setShortcut("Ctrl+T")
        brush_color.addAction(yellow_action)
        yellow_action.triggered.connect(self.yellowColor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            # print(self.lastPoint)

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def onePixel(self):
        self.brush_size = 1

    def threePixel(self):
        self.brush_size = 3

    def fivePixel(self):
        self.brush_size = 5

    def sevenPixel(self):
        self.brush_size = 7

    def ninePixel(self):
        self.brush_size = 9

    def blackColor(self):
        self.brush_color = Qt.black

    def blueColor(self):
        self.brush_color = Qt.blue

    def redColor(self):
        self.brush_color = Qt.red

    def greenColor(self):
        self.brush_color = Qt.green

    def yellowColor(self):
        self.brush_color = Qt.yellow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()