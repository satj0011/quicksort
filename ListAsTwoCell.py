# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

class MethodNotDefinedForThisPositionError(Exception):
    pass
"""
Datatypen Lista enligt definitionen p� sidan 44 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar listan med hj�lp av en 2-Cell
"""
from TwoCell import TwoCell

class List:

    def __init__(self):
        """
            Syfte: Skapar en tom lista med en tom 2-Cell som "huvud" i listan.
            Returv�rde: -
            Kommentarer: I boken heter denna funktion Empty. Vi ser till att
                         First(lista) = Last(lista)
        """
        self._head= TwoCell()
        self._head.setPrev(self._head)
        self._head.setNext(self._head)

    def insert(self, position, obj):
        """
            Syfte: Stoppar in ett nytt element med v�rdet obj i listan f�re
                        angiven position
            Parametrar: position - En position i listan
                        obj - v�rdet som ska in i listan
            Returv�rde: Positionen f�r det insatta elemenet
            Kommentarer: 
        """        
        newCell = TwoCell()
        newCell.setValue(obj)
        if self.isempty():
            newCell.setPrev(self._head)
            newCell.setNext(self._head)
            self._head.setPrev(newCell)
            self._head.setNext(newCell)
        else:
            newCell.setPrev(position.inspectPrev())
            newCell.setNext(position)
            position.setPrev(newCell)
            newCell.inspectPrev().setNext(newCell)            
        return newCell

    def isempty(self):
        """
            Syfte: Returnerar sant om listan �r tom (saknar element)
            Parametrar: -
            Returv�rde: Sant om listan �r tom
            Kommentarer:
        """    
        return (self._head.inspectPrev()== self._head) and (self._head.inspectNext() == self._head)

    def inspect(self,position):
        """
            Syfte: Returnerar v�rdet som finns p� angiven position
            Parametrar: position - En position i listan
            Returv�rde: V�rdet som finns p� angiven position
            Kommentarer: Inte definierad f�r listans sista position
        """    
        if position == self.end():
            raise MethodNotDefinedForThisPositionError("Error in inspect")          
        return position.inspectValue();

    def first(self):
        """
            Syfte: Returnerar listans f�rsta position
            Parametrar: -
            Returv�rde: Listans f�rsta position
            Kommentarer:
        """    
        return self._head.inspectNext()

    def end(self):
        """
            Syfte: Returnerar listans sista position
            Parametrar: -
            Returv�rde: Listans f�rsta position
            Kommentarer:
        """    
        return self._head

    def next(self,position):
        """
            Syfte: Returnerar position efter den angivna positionen
            Parametrar: position - En position i listan
            Returv�rde: Positionen efter den angivna
            Kommentarer: Inte definierad f�r listans sista position
                        (som saknar element)
        """    
        if position == self.end():
                    raise MethodNotDefinedForThisPositionError("Error in next")                 
        return position.inspectNext()

    def previous(self,position):
        """
            Syfte: Returnerar position f�re den angivna positionen
            Parametrar: position - En position i listan
            Returv�rde: Positionen f�re den angivna
            Kommentarer: Inte definierad f�r listans f�rsta position
        """    
        if position == self.first():
                    raise MethodNotDefinedForThisPositionError("Error in previous")                 
        return position.inspectPrev()

    def remove(self,position):
        """
            Syfte: Tar bort elementet p� den angivna positionen 
            Parametrar: position - En position i listan
            Returv�rde: Positionen p� elementet direkt efter det som togs bort
            Kommentarer: �r inte definierad f�r listans sista position
                        (som saknar element)
        """    
        if position == self.end():
                    raise MethodNotDefinedForThisPositionError("Error in remove")                 
        position.inspectPrev().setNext(position.inspectNext())
        position.inspectNext().setPrev(position.inspectPrev())
        
        return position.inspectNext()
