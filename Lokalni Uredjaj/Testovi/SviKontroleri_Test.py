import unittest
import sys

from LokalniUredjaj.Uredjaj_funkcije import SviKontroleri

sys.path.insert(0,'C:\\Users\\MSI\\Documents\\GitHub\\res-tim19\\Lokalni Kontroler\\Model\\ListaKontrolera.xml')


class MyTestCase(unittest.TestCase):
    def test_validan(self):
        Dict2 = {}
        Dict1 = SviKontroleri()
        Dict2["50002"] = "k1"
        self.assertEqual(Dict1, Dict2)

    def test_nepostojeciPort(self):
        Dict2 = {}
        Dict1 = SviKontroleri()
        Dict2[""] = "k1"
        self.assertNotEqual(Dict1, Dict2)

    def test_nepostojeciKontroler(self):
        Dict2 = {}
        Dict1 = SviKontroleri()
        Dict2["50002"] = ""
        self.assertNotEqual(Dict1, Dict2)

    def test_pogresanport(self):
        Dict1 = SviKontroleri()
        Dict2 = {}
        Dict2["60007"] = "k1"
        self.assertNotEqual(Dict1, Dict2)

    def test_pogresankontroler(self):
        Dict1 = SviKontroleri()
        Dict2 = {}
        Dict2["50002"] = "p1"
        self.assertNotEqual(Dict1, Dict2)

if __name__ == '__main__':
    unittest.main()



