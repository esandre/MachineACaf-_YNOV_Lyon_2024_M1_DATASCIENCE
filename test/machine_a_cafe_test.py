import unittest

from machine_a_cafe import MachineACafé
from utilities.brewer_surveillant_les_appels import BrewerSurveillantLesAppels
from utilities.lecteur_cb_pour_les_tests import LecteurCbPourLesTests


class MyTestCase(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine a café
        lecteur_cb = LecteurCbPourLesTests()
        brewer = BrewerSurveillantLesAppels()
        MachineACafé(brewer, lecteur_cb)

        # QUAND une carte est détectée
        lecteur_cb.simuler_carte_détectée()

        # ALORS un café est commandé au hardware
        self.assertTrue(brewer.make_a_coffee_appelé())

    def test_sans_detection_cb(self):
        # ETANT DONNE une machine a café
        lecteur_cb = LecteurCbPourLesTests()
        brewer = BrewerSurveillantLesAppels()
        MachineACafé(brewer, lecteur_cb)

        # QUAND aucune carte n'est détectée

        # ALORS aucun café n'est commandé au hardware
        self.assertFalse(brewer.make_a_coffee_appelé())


if __name__ == '__main__':
    unittest.main()
