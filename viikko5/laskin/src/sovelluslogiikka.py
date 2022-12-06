class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.viime_tulos = tulos

class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovelluslogiikka.viime_tulos = self.sovelluslogiikka.tulos
        syote = int(self.lue_syote())
        self.sovelluslogiikka.tulos += syote

    def kumoa(self):
        self.sovelluslogiikka.tulos = self.sovelluslogiikka.viime_tulos

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovelluslogiikka.viime_tulos = self.sovelluslogiikka.tulos
        syote = int(self.lue_syote())
        self.sovelluslogiikka.tulos -= syote


    def kumoa(self):
        self.sovelluslogiikka.tulos = self.sovelluslogiikka.viime_tulos

class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    
    def suorita(self):
        self.sovelluslogiikka.viime_tulos = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.tulos = 0

    def kumoa(self):
        self.sovelluslogiikka.tulos = self.sovelluslogiikka.viime_tulos

class Kumoa:
    def __init__(self, sovelluslogiikka, lue_viime_komento):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_viime_komento = lue_viime_komento

    def suorita(self):
        self.lue_viime_komento().kumoa()

    def kumoa(self):
        pass
