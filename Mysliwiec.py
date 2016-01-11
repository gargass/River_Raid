import random

from Obiekt import Obiekt
from Rakieta2 import Rakieta2
from Stale import MYSLIWIEC, SPEED


class Mysliwiec(Obiekt):
    def __init__(self, x, y):
        super(Mysliwiec, self).__init__(x, y, 30, 40, MYSLIWIEC)
        self.speed = 2
        self.strzal = 2
        self.czy_wrog = True

    def Move(self):
        y = random.randint(1,self.speed)
        x = random.randint(-self.speed, self.speed)
        self.UstawPozycje(self.S.x() + x * SPEED, self.S.y() + y * SPEED)

    def Wystrzal(self, lista, czas):
        if czas % (self.strzal * 150) == 0:
            rakieta = Rakieta2(self.S.x(), self.S.y())
            lista.append(rakieta)
