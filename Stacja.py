from Obiekt import Obiekt
from Stale import STACJA, SPEED


class Stacja(Obiekt):
    def __init__(self, x, y):
        super(Stacja, self).__init__(x, y, 20, 20, STACJA)

    def Move(self):
        self.UstawPozycje(self.S.x(), self.S.y() + SPEED)