
from .obiekt import Obiekt
from ..stale import *


class Rakieta2(Obiekt):
    def __init__(self, x, y):
        super(Rakieta2, self).__init__(x, y, 15, 20, RAKIETA_2)
        self.speed = 4
        self.czy_wrog = True

    def Move(self):
        self.UstawPozycje(self.S.x(), self.S.y() + self.speed * SPEED)