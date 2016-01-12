from .obiekt import *


class Bomba(Obiekt):
    def __init__(self, x, y):
        super(Bomba, self).__init__(x, y, 20, 20, BOMBA)

    def Move(self):
        self.UstawPozycje(self.S.x(), self.S.y() + SPEED)