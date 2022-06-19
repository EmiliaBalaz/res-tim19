import unittest 

import mock
from LokalniUredjaj.Uredjaj_funkcije import PonovoUnesiStanjeD

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        state = "ON"
        with mock.patch('builtins.input',return_value = state):
            temp = PonovoUnesiStanjeD(state)

            self.assertEqual(temp,"True")

    
    def test_case2(self):
        state = "OFF"
        with mock.patch('builtins.input',return_value = state):
            temp = PonovoUnesiStanjeD(state)

            self.assertEqual(temp,"True")

    def test_case3(self):
        state = "OPEN"
        with mock.patch('builtins.input',return_value = state):
            temp = PonovoUnesiStanjeD(state)

            self.assertEqual(temp,"True")
    
    def test_case4(self):
        state = "CLOSE"
        with mock.patch('builtins.input',return_value = state):
            temp = PonovoUnesiStanjeD(state)

            self.assertEqual(temp,"True")
    def test_case5(self):
        state = "sdaf"
        with mock.patch('builtins.input',return_value = state):
            temp1 = PonovoUnesiStanjeD(state)

            self.assertEqual(temp1,"ERROR")
    
    def test_case6(self):
        state = 1
        with mock.patch('builtins.input',return_value = state):
            temp1 = PonovoUnesiStanjeD(state)

            self.assertEqual(temp1,"ERROR")


if __name__ == '__main__':
    unittest.main()