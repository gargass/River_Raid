import random

from PyQt4 import QtGui, QtCore

from Balon import Balon
from Bomba import Bomba
from Most import Most
from Mysliwiec import Mysliwiec
from Porazka import Porazka
from Rakieta1 import Rakieta1
from Rakieta2 import Rakieta2
from Rzeka import Rzeka
from Samolot import Samolot
from Stacja import Stacja
from Statek import Statek
from Stale import WIDTH_GAME


class Game(QtGui.QWidget):
    def __init__(self, view):
        super(Game, self).__init__()

        self.samolot = Samolot()
        self.rzeka = Rzeka()
        self.lista_friend = []
        self.lista_enemy = []

        self.Parametry(0)

        self.view = view
        self.key = 'supa'

        self.punkty = 0

        self.poziom = 1
        self.przejscie = 0
        self.czas = 0

    def Parametry(self, plus):
        self.stepBalon = 2 + plus
        self.stepBomby = 15 + plus
        self.stepMysliwiec = 0 if plus < 2 else 4 + plus
        self.stepStatki = 0 if plus < 1 else 3 + plus
        self.stepStacje = 4

        self.razy = 150
        self.max_elementow = 15

    def keyPressEvent(self, QKeyEvent):
        self.key = QKeyEvent.key()

    def WstawBalony(self, N):
        for n in range(N):
            balon = Balon(0, 0)
            x = random.uniform(0 + balon.NW.x(), WIDTH_GAME - balon.NE.x())
            y = random.gammavariate(1,1)
            balon.UstawPozycje(x,y)
            self.lista_enemy.append(balon)

    def WstawStatki(self, N):
        for n in range(N):
            statek = Statek(1 / 2 * WIDTH_GAME, 0)
            x = random.uniform(30 + statek.NW.x(), WIDTH_GAME - statek.NE.x() - 40)
            y = random.gammavariate(1,1)
            statek.UstawPozycje(x,y)
            self.lista_enemy.append(statek)

    def WstawStacje(self, N):
        for n in range(N):
            stacja = Stacja(0, 0)
            x = random.uniform(0 + stacja.NW.x(), WIDTH_GAME - stacja.NE.x())
            y = random.gammavariate(1,1)
            stacja.UstawPozycje(x,y)
            self.lista_friend.append(stacja)

    def WstawMysliwce(self, N):
        for n in range(N):
            mysliwiec = Mysliwiec(0, 0)
            x = random.uniform(0 + mysliwiec.NW.x(), WIDTH_GAME - mysliwiec.NE.x())
            y = random.gammavariate(1,1)
            mysliwiec.UstawPozycje(x,y)
            self.lista_enemy.append(mysliwiec)

    def WstawBomby(self, N):
        for n in range(N):
            bomba = Bomba(0, 0)
            x = random.uniform(0 + bomba.NW.x(), WIDTH_GAME - bomba.NE.x())
            bomba.UstawPozycje(x, bomba.S.y())
            self.lista_friend.append(bomba)

    def WstawMost(self):
        if self.czas/10000 == self.poziom:
            most = Most()
            self.lista_friend.append(most)


    def ZwiekszPoziom(self):
        if self.samolot.czy_istnieje:
            self.WstawMost()

            for el in self.lista_friend:
                if el.czy_istnieje and type(el) == Most:

                    if int(el.NW.y()) == int(self.samolot.SW.y()):
                        self.Parametry(self.poziom)
                        self.poziom += 1
                        el.czy_istnieje = False
                        return True
            return False


    def czyPorazka(self):
        if self.samolot.zycie == 0 and self.samolot.czy_istnieje:
            self.samolot.czy_istnieje = False
            porazka = Porazka()
            self.lista_friend.append(porazka)
            return True
        return False


    def drawBoard(self, view):
        self.rzeka.drawObiekt(view.scene)

        self.lista_enemy = sorted(self.lista_enemy, key=lambda obiekt: -obiekt.warstwa)
        for el in self.lista_enemy:
            el.drawObiekt(view.scene)

        self.lista_friend = sorted(self.lista_friend, key=lambda obiekt: -obiekt.warstwa)
        for el in self.lista_friend:
            el.drawObiekt(view.scene)

        self.samolot.drawObiekt(view.scene)

    def Czy_zderzenie(self, obiekt1, obiekt2):

        rect = QtCore.QRectF(obiekt1.NW, obiekt1.SE)
        if rect.contains(obiekt2.NW) or rect.contains(obiekt2.NE) or rect.contains(obiekt2.SW) or rect.contains(obiekt2.SE):
            return True

        return False


    def Trafienie_bonus(self):
        for el in self.lista_friend:
            if el.czy_istnieje and self.Czy_zderzenie(el, self.samolot):
                if type(el) == Stacja:
                    self.samolot.paliwo = min(self.samolot.paliwo + 20, 100)
                    el.czy_istnieje = False

                if type(el) == Bomba:
                    for enemy in self.lista_enemy:
                        enemy.czy_istnieje = False
                    el.czy_istnieje = False

    def Trafienie_we_wroga(self):
        for el_friend in self.lista_friend:
            if el_friend.czy_istnieje and type(el_friend) == Rakieta1:
                for el_enemy in self.lista_enemy:
                    if el_enemy.czy_istnieje and self.Czy_zderzenie(el_enemy, el_friend):
                        if not type(el_enemy) == Rakieta2:
                            self.punkty += 1
                        el_enemy.czy_istnieje = False
                        el_friend.czy_istnieje = False

    def Trafienie_w_samolot(self):
        for el_enemy in self.lista_enemy:
            if el_enemy.czy_istnieje and self.Czy_zderzenie(el_enemy, self.samolot):
                self.samolot.zycie -= 1
                el_enemy.czy_istnieje = False


    def Move(self):
        self.samolot.Move(self.key)
        for el in self.lista_friend:
            el.Move()
        for el in self.lista_enemy:
            el.Move()

        self.rzeka.Move()

        self.czas += 1

    def UsunZmarlych(self):
        for el in self.lista_enemy:
            el.UstawZycie()
            if not el.czy_istnieje:
                self.lista_enemy.remove(el)
        for el in self.lista_friend:
            el.UstawZycie()
            if not el.czy_istnieje:
                self.lista_friend.remove(el)


    def LosowoBalony(self):
        czy = random.choice([0,1])
        if self.stepBalon and czy and self.czas % (self.stepBalon * self.razy)  == 0:
            self.WstawBalony(1)

    def LosowoStacje(self):
        czy = random.choice([0,1])
        if self.stepStacje and czy and self.czas % (self.stepStacje * self.razy)  == 0:
            self.WstawStacje(1)

    def LosowoMysliwce(self):
        czy = random.choice([0,1])
        if self.stepMysliwiec and czy and self.czas % (self.stepMysliwiec * self.razy)  == 0:
            self.WstawMysliwce(1)


    def LosowoStatki(self):
        czy = random.choice([0,1])
        if self.stepStatki and czy and self.czas % (self.stepStatki * self.razy) == 0:
            self.WstawStatki(1)

    def LosowoWystrzal(self):
        for el in self.lista_enemy:
            if type(el) == Mysliwiec:
                czy = random.choice([0,0,0,1])
                if czy:
                    el.Wystrzal(self.lista_enemy, self.czas)

    def LosowoBomby(self):
        czy = random.choice([0,1])
        if self.stepBomby and czy and self.czas % (self.stepBomby * self.razy) == 0:
            self.WstawBomby(1)



    def timerEvent(self, e):

        self.czyPorazka()
        self.UsunZmarlych()

        #if self.max_elementow >= len(self.lista_enemy):
        if not self.ZwiekszPoziom():
            self.LosowoBalony()
            self.LosowoStatki()
            self.LosowoStacje()
            self.LosowoBomby()
            self.LosowoMysliwce()
            self.LosowoWystrzal()

        if self.samolot.Wystrzal(self.lista_friend, self.key):
            self.key = 'dupa'


        self.Move()
        self.Trafienie_bonus()
        self.Trafienie_we_wroga()
        self.Trafienie_w_samolot()
        self.UsunZmarlych()

        self.WstawMost()
        self.ZwiekszPoziom()


        self.view.scene.clear()
        self.drawBoard(self.view)
