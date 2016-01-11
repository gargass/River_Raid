from PyQt4 import QtGui, QtCore

from CentralWidget import CentralWidget
from Stale import WIDTH_GAME, HEIGHT_GAME, ABOUT

class About(QtGui.QWidget):
    def __init__(self):
        super(About, self).__init__()

        self.initAbout()

    def initAbout(self):
        file = open(ABOUT)
        text = file.read()
        aboutLabel = QtGui.QLabel(text, self)
        aboutLabel.setGeometry(0,0,400, 400)
        self.setWindowTitle('River Raid - About')

class Opcje(QtGui.QWidget):
    def __init__(self):
        super(Opcje, self).__init__()
        self.initOpcje()

    def initOpcje(self):

        self.zuzycie = 0.5

        sldZuzycie = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sldZuzycie.setFocusPolicy(QtCore.Qt.NoFocus)
        sldZuzycie.setGeometry(30, 40, 100, 30)
        sldZuzycie.valueChanged[int].connect(self.ustawZuzycie)

        self.label = QtGui.QLabel('Zużycie paliwa', self)
        self.label.setPixmap(QtGui.QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)

    def ustawZuzycie(self):
        





class Menu(QtGui.QMainWindow):

    def __init__(self):
        super(Menu, self).__init__()

        self.iniiMenu()


    def iniiMenu(self):
        self.tboard = CentralWidget()
        #self.tboard = Example()
        self.setCentralWidget(self.tboard)


        closeAction = QtGui.QAction(QtGui.QIcon('samolot_1.jpg'), 'Close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Close application')
        closeAction.triggered.connect(QtCore.QCoreApplication.instance().quit)

        optionsAction = QtGui.QAction(QtGui.QIcon('samolot_1.jpg'), 'Options', self)
        optionsAction.setShortcut('Ctrl+O')
        optionsAction.setStatusTip('Options')
        #optionsAction.triggered.connect(QtCore.QCoreApplication.instance().quit)


        self.about = About()
        aboutAction = QtGui.QAction(QtGui.QIcon('samolot_1.jpg'), 'About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.setStatusTip('About')
        aboutAction.triggered.connect(self.showAbout)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(optionsAction)

        closeMenu = menubar.addMenu('Close')
        closeMenu.addAction(closeAction)

        helpMenu = menubar.addMenu('Help')
        helpMenu.addAction(aboutAction)



        self.setGeometry(150, 20, WIDTH_GAME + 300, HEIGHT_GAME + 100)
        self.center()

        self.setWindowTitle('River Raid')
        self.show()

    def showAbout(self):
        self.about.show()

    def center(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,20)