import unittest
import mock

from LokalniUredjaj.Uredjaj_funkcije import SviKontroleri, Unos_porta


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        port = "50002"
        with mock.patch('builtins.input', return_value=port):
            unetiPort = Unos_porta()


        self.assertEqual(unetiPort, port)

    def test_case2(self):
        port=""
        with mock.patch('builtins.input', return_value=port):
            unetiPort = Unos_porta()

        self.assertEqual(unetiPort, "ERROR")

    def test_case3(self):
        port="12345"
        with mock.patch('builtins.input', return_value=port):
            unetiPort = Unos_porta()

        self.assertEqual(unetiPort, "ERROR");

    def test_case4(self):
        port = "abc"
        with mock.patch('builtins.input', return_value=port):
            unetiPort = Unos_porta()

        self.assertEqual(unetiPort, "ERROR");


if __name__ == '__main__':
    unittest.main()
