from PyQt4 import QtGui, QtCore


class Opcje(QtGui.QWidget):
    def __init__(self, x, y, callback):
        super(Opcje, self).__init__()

        self.callback = callback

        self.menu = QtGui.QVBoxLayout()
        self.initOpcje(x, y)

    def initOpcje(self, x, y):


        self.ile_balon = 2
        self.ile_bomba = 15
        self.ile_mysliwiec = 4
        self.ile_statek = 3
        self.ile_stacja = 4

        self.opcjeLayout = QtGui.QVBoxLayout()
        self.stworzZuzycie()
        self.stworzBalon()
        self.stworzBomba()

        self.setLayout(self.opcjeLayout)
        self.setWindowTitle('Opcje')
        self.setGeometry(x, y, 200, 300)
        czcionka = QtGui.QFont('Decorative', 15)
        self.okButton = QtGui.QPushButton('Start', self)
        self.okButton.setFont(czcionka)
        self.okButton.setToolTip('Kliknij, by potwierdź')
        self.okButton.resize(self.okButton.sizeHint())

        self.okButton.clicked.connect(self.funkcjaOK)
        self.okButton.setGeometry(200, 200, 50, 50)


    def stworzZuzycie(self):
        self.ile_zuzycie = 0.5
        layout = QtGui.QVBoxLayout()
        layout1 = QtGui.QHBoxLayout()

        label = QtGui.QLabel('Zużycie paliwa', self)
        label.setFont(QtGui.QFont('Decorative', 10))

        self.zuzycie_label = QtGui.QLabel(str(self.ile_zuzycie), self)
        self.zuzycie_label.setFont(QtGui.QFont('Decorative', 10))
        sldZuzycie = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sldZuzycie.setFocusPolicy(QtCore.Qt.NoFocus)
        sldZuzycie.valueChanged[int].connect(self.ustawZuzycie)

        layout1.addWidget(sldZuzycie)
        layout1.addWidget(self.zuzycie_label)
        layout.addWidget(label)
        layout.addLayout(layout1)
        self.opcjeLayout.addLayout(layout)


    def stworzBomba(self):
        self.ile_bomba = 15
        layout = QtGui.QVBoxLayout()
        layout1 = QtGui.QHBoxLayout()

        label = QtGui.QLabel('Czestosc bomb', self)
        label.setFont(QtGui.QFont('Decorative', 10))

        self.bomba_label = QtGui.QLabel(str(self.ile_bomba), self)
        self.bomba_label.setFont(QtGui.QFont('Decorative', 10))
        sldBomba = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sldBomba.setFocusPolicy(QtCore.Qt.NoFocus)
        sldBomba.valueChanged[int].connect(self.ustawBomba)

        layout1.addWidget(sldBomba)
        layout1.addWidget(self.bomba_label)
        layout.addWidget(label)
        layout.addLayout(layout1)
        self.opcjeLayout.addLayout(layout)







    def stworzBalon(self):
        self.balon = 2
        layout = QtGui.QVBoxLayout()
        layout1 = QtGui.QHBoxLayout()

        label = QtGui.QLabel('Czestosc balonow', self)
        label.setFont(QtGui.QFont('Decorative', 10))

        self.balon_label = QtGui.QLabel(str(self.balon), self)
        self.balon_label.setFont(QtGui.QFont('Decorative', 10))
        sldBalon = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sldBalon.setFocusPolicy(QtCore.Qt.NoFocus)
        sldBalon.valueChanged[int].connect(self.ustawBalon)

        layout1.addWidget(sldBalon)
        layout1.addWidget(self.balon_label)
        layout.addWidget(label)
        layout.addLayout(layout1)
        self.opcjeLayout.addLayout(layout)

    def ustawZuzycie(self, z):
        self.ile_zuzycie = z / 100
        self.zuzycie_label.setText(str(z/100))

    def ustawBalon(self, b):
        self.ile_balon = b
        self.balon_label.setText(str(b / 10))

    def ustawBomba(self, b):
        self.ile_bomba = b
        self.bomba_label.setText(str(b/10))


    def funkcjaOK(self):
        self.callback(self.ile_zuzycie, self.ile_balon, self.ile_bomba)