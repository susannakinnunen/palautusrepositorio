import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), maito.hinta())

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä",2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä",2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), maito.hinta()*2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        tuotteen_nimi = ostos.tuotteen_nimi()
        tuotteen_lukumaara = ostos.lukumaara()

        self.assertEqual(f"Tuotteen nimi: {tuotteen_nimi} ja lukumäärä: {tuotteen_lukumaara}", "Tuotteen nimi: Maito ja lukumäärä: 1")


    def test_kahden_eri_tuotteen_lisaamisen_jälkeen_ostoskori_sisältää_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä",2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumaara_2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(f"ostoksen nimi: {ostokset[0].tuotteen_nimi()} ja lukumäärä {ostokset[0].lukumaara()}", "ostoksen nimi: Maito ja lukumäärä 2")

    
    def test_jos_korissa_on_kaksi_samaa_tuotetta_ja_toinen_naista_poistetaan_jaa_koriin_ostos_jossa_on_tuotetta_1(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(f"ostoksen nimi: {ostokset[0].tuotteen_nimi()} ja lukumäärä {ostokset[0].lukumaara()}", "ostoksen nimi: Maito ja lukumäärä 1")

    
    def test_jos_koriin_on_lisatty_tuote_ja_sama_tuote_poistetaan_on_kori_taman_jalkeen_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        self.assertEqual(f"tavaroita korissa: {self.kori.tavaroita_korissa()}, hinta: {self.kori.hinta()}", "tavaroita korissa: 0, hinta: 0")

    def test_koriin_on_lisatty_tuotteita_ja_kori_tyhjennetaan_jolloin_korissa_ei_ole_tuotteita(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä",2)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.kori.tyhjenna()

        self.assertEqual(f"tavaroita korissa: {self.kori.tavaroita_korissa()}, hinta: {self.kori.hinta()}", "tavaroita korissa: 0, hinta: 0")

        