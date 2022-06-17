import unittest

import mock
from datetime import datetime
from LokalniUredjaj.Uredjaj_funkcije import PromenaStanjaAnalognogUredjaja


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        state = "5"
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjaAnalognogUredjaja(idDigital)

        self.assertEqual(msg, idDigital + "/" + str(datetime.now()) + "/" + state)

    def test_case2(self):
        state = "abc"
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjaAnalognogUredjaja(idDigital)

        self.assertEqual(msg, "ERROR")

    def test_case3(self):
        state = " "
        with mock.patch('builtins.input', return_value=state):
            idDigital = "1"
            msg = PromenaStanjaAnalognogUredjaja(idDigital)

        self.assertEqual(msg, "ERROR")

if __name__ == '__main__':
    unittest.main()
