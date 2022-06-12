from datetime import datetime
import threading
import time
import unittest
import socket
import mock

from LOKALNI_UREDJAJ.LokalniUredjaj.Uredjaj_funkcije import UnosAnalognogUredjaja






class MyTestCase(unittest.TestCase):
    def test_case1(self):

        with mock.patch('builtins.input', return_value="OFF"):
            id,str=UnosAnalognogUredjaja()
            self.assertEqual(str, "ERROR")
            self.assertEqual(id,"")

    def test_case2(self):

        with mock.patch('builtins.input', return_value="1"):
            id,string=UnosAnalognogUredjaja()

            self.assertEqual(string, "1/"+str(datetime.now())+"/1")
            self.assertEqual(id,"1")

if __name__ == '__main__':
    unittest.main()

