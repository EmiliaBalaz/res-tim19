import unittest 

import threading
import socket
import time

import mock
from LokalniUredjaj.Uredjaj_funkcije import PonovoUnesiStanjeA

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        state = 1.1
        with mock.patch('builtins.input',return_value = state):
            temp = PonovoUnesiStanjeA(state)

            self.assertNotEqual(temp,"ERROR")

    
    def test_case2(self):
        state = 1
        with mock.patch('builtins.input',return_value = state):
            temp1 = PonovoUnesiStanjeA(state)

            self.assertEqual(temp1,int(state))

if __name__ == '__main__':
    unittest.main()

