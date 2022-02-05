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

Denna klass implementerar listan med hj�lp av en array
"""
class List:

    def __init__(self):
        """
            Syfte: Skapar en tom lista med hj�lp av en array
            Returv�rde: -
            Kommentarer: I boken heter denna funktion Empty. Vi ser till att
                         First(lista) = Last(lista).
                         Notera att det finns en maxstorlek!
        """
        self._MAX = 20
        self._values = [None for _ in range(self._MAX)]
        self._endpos = 0    # F�rsta tomma platsen i arrayen
        
    def insert(self, position, obj):
        """
            Syfte: Stoppar in ett nytt element med v�rdet obj i listan f�re
                        angiven position
            Parametrar: position - En position i listan
                        obj - v�rdet som ska in i listan
            Returv�rde: Positionen f�r det insatta elemenet
            Kommentarer: Odefinierat vad som h�nder f�r en felaktig position
        """        
        if (position < 0) or (position >  self._endpos):
            raise MethodNotDefinedForThisPositionError("Error in insert")         
        if not self.isempty():
            for i in range(self._endpos, position, -1):
                self._values[i] = self._values[i-1]
        
        self._values[position] = obj
        self._endpos = self._endpos + 1
            
        return position

    def isempty(self):
        """
            Syfte: Returnerar sant om listan �r tom (saknar element)
            Parametrar: -
            Returv�rde: Sant om listan �r tom
            Kommentarer:
        """    
        return self._endpos==0

    def inspect(self,position):
        """
            Syfte: Returnerar v�rdet som finns p� angiven position
            Parametrar: position - En position i listan
            Returv�rde: V�rdet som finns p� angiven position
            Kommentarer: Inte definierad f�r listans sista position
        """    
        if position == self._endpos:
            raise MethodNotDefinedForThisPositionError("Error in inspect")          
        return self._values[position]

    def first(self):
        """
            Syfte: Returnerar listans f�rsta position
            Parametrar: -
            Returv�rde: Listans f�rsta position
            Kommentarer:
        """    
        return 0

    def end(self):
        """
            Syfte: Returnerar listans sista position
            Parametrar: -
            Returv�rde: Listans f�rsta position
            Kommentarer:
        """    
        return self._endpos

    def next(self,position):
        """
            Syfte: Returnerar position efter den angivna positionen
            Parametrar: position - En position i listan
            Returv�rde: Positionen efter den angivna
            Kommentarer: Inte definierad f�r listans sista position
                        (som saknar element)
        """    
        if position == self._endpos:
            raise MethodNotDefinedForThisPositionError("Error in next")            
        return position + 1

    def previous(self,position):
        """
            Syfte: Returnerar position f�re den angivna positionen
            Parametrar: position - En position i listan
            Returv�rde: Positionen f�re den angivna
            Kommentarer: Inte definierad f�r listans f�rsta position
        """    
        return position - 1

    def remove(self,position):
        """
            Syfte: Tar bort elementet p� den angivna positionen 
            Parametrar: position - En position i listan
            Returv�rde: Positionen p� elementet direkt efter det som togs bort
            Kommentarer: �r inte definierad f�r listans sista position
                        (som saknar element)
        """    
        if position == self._endpos:
            raise MethodNotDefinedForThisPositionError("Error in remove")  
        for i in range(position, self._endpos):
            self._values[i] = self._values[i+1]
        
        self._endpos = self._endpos - 1
        return position
    
