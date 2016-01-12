from PyQt4 import QtCore


from .obiekt import Obiekt
from .rakieta1 import Rakieta1
from ..stale import *


class Samolot(Obiekt):
    def __init__(self):
        super(Samolot, self).__init__(0, HEIGHT_GAME-20, 50, 40, SAMOLOT)

        self.zycie = 3
        self.speed = 2

        self.paliwo = 100
        self.zuzycie = 0.5
        self.UstawPozycje(1/2*WIDTH_GAME, HEIGHT_GAME-20)
        self.UstawWarstwe(0)

    def Wystrzal(self, lista, key):
        if self.czy_istnieje and key == QtCore.Qt.Key_W:

            rakieta = Rakieta1(self.S.x(), self.S.y())
            lista.append(rakieta)
            return True
        return False

    def ZuzyjPaliwo(self):
        if self.czy_istnieje:
            self.paliwo = max(0,self.paliwo - self.zuzycie*0.1*SPEED)
            if self.paliwo == 0:
                self.zycie = 0


    def Move(self, key):
        if self.czy_istnieje:
            if key == QtCore.Qt.Key_A:
                self.UstawPozycje(max(self.S.x() - self.speed * SPEED, 0 + 1/2*self.w), self.S.y())
            if key == QtCore.Qt.Key_D:
                self.UstawPozycje(min(self.S.x() + self.speed * SPEED, WIDTH_GAME - 1/2*self.w), self.S.y())

            self.ZuzyjPaliwo()

    def PodajPozycje(self):
        return self.x

    def PodajPaliwo(self):
        return self.paliwo