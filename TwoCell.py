# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

"""
Datatypen 2-Cell enligt definitionen p� sidan 77 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7

Implementationen avviker s� tillvida att link1 kallas prev och link2 kallas next
eftersom cellen fr�mst ska anv�ndas i listor och det underl�ttar l�sandet av koden.

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

"""
class TwoCell:
    def __init__(self):
        """
            Syfte: Skapar en ny cell utan definierat v�rde eller l�nkar
            Parametrar: -
            Returv�rde: -
            Kommentarer: I definitionen heter denna funktion Create
        """
        self._data = None
        self._prev = None
        self._next = None

    def setValue(self,data):
        """
            Syfte: S�tter cellens v�rde till data
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        self._data = data

    def setPrev(self,link):
        """
            Syfte: S�tter cellens prev-l�nk till link
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        self._prev =link

    def setNext(self,link):
        """
            Syfte: S�tter cellens next-l�nk till link
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        self._next =link

    def inspectValue(self):
        """
            Syfte: Returnerar cellens v�rde 
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        return self._data

    def inspectPrev(self):
        """
            Syfte: Returnerar cellens prev-l�nk 
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        return self._prev

    def inspectNext(self):
        """
            Syfte: Returnerar cellens next-l�nk
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        return self._next
