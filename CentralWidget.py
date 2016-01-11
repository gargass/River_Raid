from PyQt4 import QtGui, QtCore

from Game import Game
from Stale import WIDTH_GAME, HEIGHT_GAME


class CentralWidget(QtGui.QWidget):

    def __init__(self):
        super(CentralWidget, self).__init__()
        self.buttonBox = QtGui.QVBoxLayout()
        self.wynikBox = QtGui.QVBoxLayout()

        self.initUI()

    def initUI(self):


        self.step = 0
        self.czyPorazka = False


        Canvas = QtGui.QGraphicsScene(0,0,WIDTH_GAME, HEIGHT_GAME)

        view = QtGui.QGraphicsView()
        view.scene = Canvas
        view.setScene(Canvas)
        view.setMaximumSize(WIDTH_GAME+10, HEIGHT_GAME+20)

        self.game = Game(view)
        self.game.drawBoard(view)

        self.stworzStart()
        self.stworzPoziom()
        self.stworzPunkty()
        self.stworzZycie()
        self.stworzPaliwo()

        menu = QtGui.QVBoxLayout()
        menu.addLayout(self.buttonBox)
        menu.addLayout(self.wynikBox)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(menu)
        hbox.addWidget(view)


        self.setLayout(hbox)

        self.timer = QtCore.QBasicTimer()

    def stworzStart(self):
        czcionka = QtGui.QFont('Decorative', 15)
        self.startButton = QtGui.QPushButton('Start', self)
        self.startButton.setFont(czcionka)
        self.startButton.setToolTip('Kliknij, by zacząć')
        self.startButton.resize(self.startButton.sizeHint())
        #self.setMaximumSize(100, 30)
        self.startButton.clicked.connect(self.doAction)
        self.buttonBox.addWidget(self.startButton)


    def stworzPunkty(self):
        czcionka = QtGui.QFont('Decorative', 15)
        punktyLabel = QtGui.QLabel('Punkty', self)
        punktyLabel.setMaximumSize(100, 30)
        punktyLabel.setFont(czcionka)
        self.punktyLCD = QtGui.QLCDNumber(self)
        self.punktyLCD.setMaximumSize(100, 70)
        self.wynikBox.addWidget(punktyLabel)
        self.wynikBox.addWidget(self.punktyLCD)

    def stworzPoziom(self):
        czcionka = QtGui.QFont('Decorative', 15)
        poziomLabel = QtGui.QLabel('Poziom', self)
        poziomLabel.setMaximumSize(100, 30)
        poziomLabel.setFont(czcionka)
        self.poziomLCD = QtGui.QLCDNumber(self)
        self.poziomLCD.setMaximumSize(100, 70)
        self.wynikBox.addWidget(poziomLabel)
        self.wynikBox.addWidget(self.poziomLCD)

    def stworzPaliwo(self):
        czcionka = QtGui.QFont('Decorative', 15)
        paliwoLabel = QtGui.QLabel('Paliwo', self)
        paliwoLabel.setMaximumSize(100, 30)
        paliwoLabel.setFont(czcionka)
        self.paliwo = QtGui.QProgressBar(self)
        self.paliwo.setMaximumSize(150, 40)
        self.wynikBox.addWidget(paliwoLabel)
        self.wynikBox.addWidget(self.paliwo)

    def stworzZycie(self):
        czcionka = QtGui.QFont('Decorative', 15)
        zycieLabel = QtGui.QLabel('Życia', self)
        zycieLabel.setMaximumSize(100, 20)
        zycieLabel.setFont(czcionka)

        self.zycieLCD = QtGui.QLCDNumber(self)
        self.zycieLCD.setMaximumSize(100, 70)
        self.wynikBox.addWidget(zycieLabel)
        self.wynikBox.addWidget(self.zycieLCD)


    def timerEvent(self, e):
        self.game.timerEvent(e)
        self.poziomLCD.display(self.game.poziom)
        self.punktyLCD.display(self.game.punkty)
        self.zycieLCD.display(self.game.samolot.zycie)
        self.paliwo.setValue(self.game.samolot.PodajPaliwo())
        self.czyPorazka = self.game.czyPorazka()



    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.startButton.setText('Start')

        else:
            self.timer.start(1, self)
            self.startButton.setText('Pauza')



    def keyPressEvent(self, QKeyEvent):
        self.game.keyPressEvent(QKeyEvent)