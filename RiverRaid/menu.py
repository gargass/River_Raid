from PyQt4 import QtGui

from .centralWidget import *
from .opcje import *
from .about import *
from .stale import *

class Menu(QtGui.QMainWindow):

    def __init__(self):
        super(Menu, self).__init__()

        self.initMenu()


    def initMenu(self):
        self.tboard = CentralWidget()

        self.setCentralWidget(self.tboard)


        closeAction = QtGui.QAction(QtGui.QIcon(SAMOLOT), 'Close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Close application')
        closeAction.triggered.connect(self.exitAction)

        self.options_active = False
        self.options = Opcje(160, 200, self.tboard.game.UstawParametry)
        optionsAction = QtGui.QAction(QtGui.QIcon(SAMOLOT), 'Options', self)
        optionsAction.setShortcut('Ctrl+O')
        optionsAction.setStatusTip('Options')
        optionsAction.triggered.connect(self.showOptions)


        self.about = About()
        aboutAction = QtGui.QAction(QtGui.QIcon(SAMOLOT), 'About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.setStatusTip('About')
        aboutAction.triggered.connect(self.showAbout)



        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(optionsAction)
        fileMenu.addAction(closeAction)

        helpMenu = menubar.addMenu('Help')
        helpMenu.addAction(aboutAction)



        self.setGeometry(150, 20, WIDTH_GAME + 300, HEIGHT_GAME + 100)
        self.center()

        self.setWindowTitle('River Raid')
        self.show()

    def showAbout(self):
        self.about.show()

    def showOptions(self):
        self.options.show()


    def center(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,20)

    def exitAction(self):

        self.options.close()
        self.close()


