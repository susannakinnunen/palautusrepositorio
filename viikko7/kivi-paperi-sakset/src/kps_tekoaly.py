from tuomari import Tuomari
from tekoaly import Tekoaly
from kivipaperisakset import KiviPaperiSakset


from tekoaly import Tekoaly

class KPSTekoaly(KiviPaperiSakset):

    def _toisen_siirto(self):
        tekoaly = Tekoaly()
        tokan_siirto = tekoaly.anna_siirto()
        return tokan_siirto