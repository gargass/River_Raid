import random

from Obiekt import Obiekt
from Stale import BALON, SPEED


class Balon(Obiekt):
    def __init__(self, x, y):
        super(Balon, self).__init__(x, y, 30, 40, BALON)
        self.speed = 1

        self.czy_wrog = True
    def Move(self):
        y = random.choice([1,1,1,2])
        x = random.choice([-2,-1,0,1,2])
        self.UstawPozycje(self.S.x() + x * SPEED, self.S.y() + y * SPEED)