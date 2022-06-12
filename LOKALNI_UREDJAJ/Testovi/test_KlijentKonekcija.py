import unittest
#import LOKALNI_UREDJAJ.LokalniUredjaj.Uredjaj_funkcije as fun
import LokalniUredjaj.Uredjaj_funkcije as fun
import mock

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        with mock.patch('builtins.input',return_value="1"):

            self.assertEqual(fun.Klijent_konekcija(), "ANALOGNI")  # add assertion here

    def test_case2(self):
        with mock.patch('builtins.input', return_value="gfhjgfghgfddffg"):
            self.assertEqual(fun.Klijent_konekcija(), "ERROR")  # add assertion here
            pass

    def test_case3(self):
        with mock.patch('builtins.input', return_value="2"):
            self.assertEqual(fun.Klijent_konekcija(), "DIGITALNI")  # add assertion here

if __name__ == '__main__':
    unittest.main()