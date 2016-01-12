
from .obiekt import Obiekt
from ..stale import *

class Rakieta1(Obiekt):
    def __init__(self, x, y):
        super(Rakieta1, self).__init__(x, y, 10, 20, RAKIETA_1)
        self.speed = 4

    def Move(self):
        self.UstawPozycje(self.S.x(), self.S.y() - self.speed * SPEED)