import unittest

from AMS import podelaPoruke, Brisaje_Dodavanje_Kontrolera


class TestAMS(unittest.TestCase):
    def test_podela_poruke(self):
        self.assertEqual(('12345678', '1655589183', '999'), podelaPoruke('12345678/1655589183/999'))

        with self.assertRaises(IndexError) as ie:
            podelaPoruke('')
        self.assertTrue(IndexError('list index out of range'), ie.exception)

    def test_dodavanje_kontrolera(self):
        self.assertEqual(('4324234', '1655589765', '123'), Brisaje_Dodavanje_Kontrolera('4324234/1655589765/123'))

        with self.assertRaises(IndexError) as ie:
            Brisaje_Dodavanje_Kontrolera('')
        self.assertTrue(IndexError('list index out of range'), ie.exception)


if __name__ == '__main__':
    unittest.main()
