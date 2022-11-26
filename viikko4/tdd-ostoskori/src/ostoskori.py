from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskorin_ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if len(self.ostoskorin_ostokset) == 0:
            return 0
        else:
            return len(self.ostoskorin_ostokset)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if len(self.ostoskorin_ostokset) == 0:
            return 0
        summa = 0
        for ostos in self.ostoskorin_ostokset:
            summa +=  ostos.hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        self.ostoskorin_ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
