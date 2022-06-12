import unittest

from datetime import datetime
import threading
import time
import unittest
import socket
import mock

from LOKALNI_UREDJAJ.LokalniUredjaj.Uredjaj_funkcije import UnosDigitalnogUredjaja



class MyTestCase(unittest.TestCase):
    def test_case1(self):
        with mock.patch('builtins.input', return_value="OPEN"):
            id, string = UnosDigitalnogUredjaja()

            self.assertEqual(string, "OPEN/"+str(datetime.now())+"/OPEN")
            self.assertEqual(id, "OPEN")

    def test_case2(self):
        with mock.patch('builtins.input',return_value="11"):
            id, string = UnosDigitalnogUredjaja()

            self.assertEqual(string, "ERROR")
            self.assertEqual(id, "")

if __name__ == '__main__':
    unittest.main()

