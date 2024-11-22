from hardware.brewer import BrewerInterface
from machine_a_cafe import MachineACafé
from utilities.brewer_surveillant_les_appels import BrewerSpy
from utilities.lecteur_cb_pour_les_tests import LecteurCbFake

class MachineACaféHarness(MachineACafé):
    def __init__(self, brewer, lecteur_cb, brewer_spy: BrewerSpy):
        super().__init__(brewer, lecteur_cb)
        self.__brewerSpy = brewer_spy

    def make_a_coffee_appelé(self):
        return self.__brewerSpy.make_a_coffee_appelé()


class MachineACaféBuilder:
    def __init__(self):
        self.__brewer = BrewerSpy()
        self.__lecteur_cb = LecteurCbFake()

    def build(self) -> MachineACaféHarness:
        return MachineACaféHarness(self.__brewer, self.__lecteur_cb, self.__brewer)

    def ayant_pour_brewer(self, brewer: BrewerInterface):
        self.__brewer = brewer
        return self

    def ayant_pour_lecteur_cb(self, lecteur_cb: BrewerInterface):
        self.__lecteur_cb = lecteur_cb
        return self

    def surveillant_le_brewer(self):
        return self.ayant_pour_brewer(BrewerSpy())