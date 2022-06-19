import unittest

from LokalniUredjaj.Uredjaj_funkcije import intTryParse


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        stanje = 1
        a = intTryParse(stanje)

        self.assertEqual(a, stanje)

    def test_case2(self):
        stanje = "a"
        a = intTryParse(stanje)

        self.assertEqual(a, "ERROR")

    def test_case3(self):
        stanje = " "
        a = intTryParse(stanje)

        self.assertEqual(a, "ERROR")


if __name__ == '__main__':
    unittest.main()
