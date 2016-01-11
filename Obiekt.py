from PyQt4 import QtCore, QtGui
from Stale import WIDTH_GAME, HEIGHT_GAME


class Obiekt(QtCore.QObject):
    def __init__(self, x, y, w, h, obraz):
        super(Obiekt, self).__init__()

        self.S = QtCore.QPointF(x, y)
        self.NW = QtCore.QPointF(x-1/2*w, y-1/2*h)
        self.NE = QtCore.QPointF(x+1/2*w, y-1/2*h)
        self.SW = QtCore.QPointF(x-1/2*w, y+1/2*h)
        self.SE = QtCore.QPointF(x+1/2*w, y+1/2*h)

        self.w = w
        self.h = h

        self.obraz = QtGui.QPixmap(obraz)
        self.obraz = self.obraz.scaled(w, h)


        self.warstwa = 10
        self.czy_wrog = False
        self.czy_istnieje = True

    def UstawPozycje(self, x, y):

        self.S = QtCore.QPointF(x, y)
        self.NW = QtCore.QPointF(x-1/2*self.w, y-1/2*self.h)
        self.NE = QtCore.QPointF(x+1/2*self.w, y-1/2*self.h)
        self.SW = QtCore.QPointF(x-1/2*self.w, y+1/2*self.h)
        self.SE = QtCore.QPointF(x+1/2*self.w, y+1/2*self.h)

    def drawObiekt(self, canvas):
        if self.czy_istnieje:
            item1 = canvas.addPixmap(self.obraz)
            item1.setPos(self.NW)

    def Move(self):
        pass

    def UstawWarstwe(self, w):
        self.warstwa = w

    def UstawZycie(self):
        if self.NW.x()>WIDTH_GAME or self.NW.y()>HEIGHT_GAME or self.SE.x()<0 or self.SE.y()<0:
            self.czy_istnieje = False