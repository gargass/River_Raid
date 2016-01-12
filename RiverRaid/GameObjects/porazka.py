
from .obiekt import Obiekt
from ..stale import *


class Porazka(Obiekt):
    def __init__(self):
        super(Porazka, self).__init__(1/2*WIDTH_GAME, 1/2*HEIGHT_GAME, 0.8*WIDTH_GAME, 70, PORAZKA)
        self.UstawWarstwe(0)