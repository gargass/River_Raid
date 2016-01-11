from Obiekt import Obiekt
from Stale import RZEKA, WIDTH_GAME, HEIGHT_GAME, SPEED


class Rzeka(Obiekt):
    def __init__(self):
        super(Rzeka, self).__init__(1/2*WIDTH_GAME, 0, WIDTH_GAME, 2*HEIGHT_GAME, RZEKA)
        self.UstawWarstwe(100)

    def Move(self):
        self.UstawPozycje(self.S.x(), self.S.y() + SPEED)
        if self.S.y() >= HEIGHT_GAME:
            self.UstawPozycje(self.S.x(), 0)