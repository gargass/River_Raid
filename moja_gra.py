import sys

from PyQt4 import QtGui

from Menu import Menu


def main():

    app = QtGui.QApplication(sys.argv)

    ex = Menu()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()