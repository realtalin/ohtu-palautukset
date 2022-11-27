from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoslista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self._ostoslista:
            tavaroita += ostos.lukumaara()
        return tavaroita

        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self._ostoslista:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        tuotetta_oli_jo_korissa = False

        # lisää tuotetta ostokseen jos sitä oli jo korissa
        for ostos in self._ostoslista:
            if lisattava == ostos.tuote:
                ostos.muuta_lukumaaraa(1)
                tuotetta_oli_jo_korissa = True
                break

        # lisää uuden ostoksen jos tuotetta ei ollut vielä korissa
        if not tuotetta_oli_jo_korissa:
            self._ostoslista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostoslista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
