KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin on oltava positiivinen kokonaisluku")

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kasvatuskoon on oltava positiivinen kokonaisluku")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujoukko = [None] * self.kapasiteetti
        self.lukuja = 0

    def luvun_indeksi(self, luku):
        for indeksi in range(0, self.lukuja):
            if luku == self.lukujoukko[indeksi]:
                return indeksi

    def kuuluu(self, luku):
        for indeksi in range(0, self.lukuja):
            if luku == self.lukujoukko[indeksi]:
                return True
                
        return False

    def taynna(self):
        if self.lukuja == self.kapasiteetti:
            return True

        return False

    def lisaa(self, luku):
        if self.lukuja == self.kapasiteetti:
            self.kasvata()

        if self.kuuluu(luku) is False:
            self.lukujoukko[self.lukuja] = luku
            self.lukuja = self.lukuja + 1
            return True

        return False

    def kasvata(self):
        vanha_lukujoukko = self.lukujoukko
        uusi_lukujoukko = [None] * (self.kapasiteetti + self.kasvatuskoko)

        for luku in range(0, self.lukuja):
            uusi_lukujoukko[luku] = vanha_lukujoukko[luku]

        self.lukujoukko = uusi_lukujoukko
        self.kapasiteetti += self.kasvatuskoko

    def poista(self, luku):
        if not self.kuuluu(luku):
            return False
            
        poistettavan_indeksi = self.luvun_indeksi(luku)
        self.lukujoukko[poistettavan_indeksi] = None
        
        for indeksi in range(poistettavan_indeksi, self.lukuja):
            self.lukujoukko[indeksi] = self.lukujoukko[indeksi+1]

        self.lukujoukko[self.lukuja] = None
        self.lukuja -= 1

    def mahtavuus(self):
        return self.lukuja

    def to_int_list(self):
        lukulista = [0] * self.lukuja

        for indeksi in range(0, self.lukuja):
            lukulista[indeksi] = self.lukujoukko[indeksi]

        return lukulista

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdistejoukko = IntJoukko()
        lukulista_a = joukko_a.to_int_list()
        lukulista_b = joukko_b.to_int_list()

        for luku in lukulista_a:
            yhdistejoukko.lisaa(luku)

        for luku in lukulista_b:
            yhdistejoukko.lisaa(luku)

        return yhdistejoukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkausjoukko = IntJoukko()
        lukulista_a = joukko_a.to_int_list()

        for luku in lukulista_a:
            if joukko_b.kuuluu(luku):
                leikkausjoukko.lisaa(luku)

        return leikkausjoukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotusjoukko = IntJoukko()
        lukulista_a = joukko_a.to_int_list()
        lukulista_b = joukko_b.to_int_list()

        for luku in lukulista_a:
            erotusjoukko.lisaa(luku)

        for luku in lukulista_b:
            erotusjoukko.poista(luku)

        return erotusjoukko

    def __str__(self):
        return "{" + ", ".join([str(luku) for luku in self.to_int_list()]) + "}"