import unittest

from LokalniUredjaj.Uredjaj_funkcije import stringTryParse


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        stanje = "ON"
        a = stringTryParse(stanje)

        self.assertEqual(a, stanje)

    def test_case2(self):
        stanje = "OFF"
        a = stringTryParse(stanje)

        self.assertEqual(a, stanje)

    def test_case3(self):
        stanje = "OPEN"
        a = stringTryParse(stanje)

        self.assertEqual(a, stanje)

    def test_case4(self):
        stanje = "CLOSE"
        a = stringTryParse(stanje)

        self.assertEqual(a, stanje)

    def test_case5(self):
        stanje = "1"
        a = stringTryParse(stanje)

        self.assertEqual(a, "ERROR")

    def test_case6(self):
        stanje = " "
        a = stringTryParse(stanje)

        self.assertEqual(a, "ERROR")

    def test_case7(self):
        stanje = "nijebroj"
        a = stringTryParse(stanje)

        self.assertEqual(a, "ERROR")


if __name__ == '__main__':
    unittest.main()
