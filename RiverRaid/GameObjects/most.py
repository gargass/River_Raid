
from .obiekt import Obiekt
from ..stale import *


class Most(Obiekt):
    def __init__(self):
        super(Most, self).__init__(1/2*WIDTH_GAME, 0, WIDTH_GAME, 30, MOST)
        self.UstawWarstwe(88)
    def Move(self):
        self.UstawPozycje(self.S.x(), self.S.y() + SPEED)