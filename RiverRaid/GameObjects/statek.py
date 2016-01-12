import random

from .obiekt import Obiekt

from ..stale import *


class Statek(Obiekt):
    def __init__(self, x, y):
        super(Statek, self).__init__(x, y, 30, 40, STATEK)
        self.speed = 1
        self.czy_wrog = True
        self.kierunek = random.choice([-1,1])

    def Move(self):
        max_left = 40
        max_right = WIDTH_GAME - 40

        self.UstawPozycje(self.S.x() + self.kierunek * self.speed * SPEED , self.S.y() + SPEED)
        if self.NW.x() < max_left or self.NE.x() > max_right:
            self.kierunek = -self.kierunek
            self.UstawPozycje(self.S.x() + self.kierunek * self.speed * SPEED , self.S.y())