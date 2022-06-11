import unittest

from LokalniUredjaj.Uredjaj_funkcije import Izlistaj_Kontrolere


class MyTestCase(unittest.TestCase):
    def test_izlistajkontrolere(self):
        Dict1 = Izlistaj_Kontrolere()
        Dict2={}
        Dict2["50002"] = "k1"
        self.assertEqual(Dict1, Dict2)

    def test_nepostojecikontroler(self):
        Dict1 = Izlistaj_Kontrolere()
        Dict2 = {}
        Dict2["50002"] = ""
        self.assertNotEqual(Dict1, Dict2)

    def test_nepostojeciport(self):
        Dict1 = Izlistaj_Kontrolere()
        Dict2 = {}
        Dict2[""] = "k1"
        self.assertNotEqual(Dict1, Dict2)

    def test_pogresanport(self):
        Dict1 = Izlistaj_Kontrolere()
        Dict2 = {}
        Dict2["60007"] = "k1"
        self.assertNotEqual(Dict1, Dict2)

    def test_pogresankontroler(self):
        Dict1 = Izlistaj_Kontrolere()
        Dict2 = {}
        Dict2["50002"] = "p1"
        self.assertNotEqual(Dict1, Dict2)

if __name__ == '__main__':
    unittest.main()
