from datetime import datetime
import unittest

import mock

from LokalniUredjaj.Uredjaj_funkcije import PromenaStanjeDigitalnogUredjaja


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        state = "OPEN"
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjeDigitalnogUredjaja(idDigital)

        self.assertEqual(msg, idDigital+"/"+str(datetime.now())+"/"+state)

    def test_case2(self):
        state = "CLOSE"
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjeDigitalnogUredjaja(idDigital)

        self.assertEqual(msg, idDigital+"/"+str(datetime.now())+"/"+state)

    def test_case3(self):
        state = "ON"
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjeDigitalnogUredjaja(idDigital)

        self.assertEqual(msg, idDigital+"/"+str(datetime.now())+"/"+state)

    def test_case4(self):
        state = "OFF"
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjeDigitalnogUredjaja(idDigital)

        self.assertEqual(msg, idDigital+"/"+str(datetime.now())+"/"+state)

    def test_case5(self):
        state = "12345"
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjeDigitalnogUredjaja(idDigital)

        self.assertEqual(msg, "ERROR")

    def test_case6(self):
        state = " "
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjeDigitalnogUredjaja(idDigital)

        self.assertEqual(msg, "ERROR")

if __name__ == '__main__':
    unittest.main()
