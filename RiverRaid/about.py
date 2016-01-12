from PyQt4 import QtGui

from RiverRaid.stale import ABOUT


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