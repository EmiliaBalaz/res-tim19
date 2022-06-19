import unittest
from unittest.mock import patch

from UI.ui_helper import UIHelper


class TestUIHelper(unittest.TestCase):
    @patch('ui_helper.print', return_value=None)
    @patch('builtins.input', return_value='1')
    def test_show_menu(self, input1, input2):
        self.assertEqual(1, UIHelper.ShowMenu(['option 1', 'option 2']))

    def test_validate_input(self):
        self.assertEqual(True, UIHelper.ValidateInput('1', 2))
        self.assertEqual(False, UIHelper.ValidateInput('3', 2))
        self.assertEqual(False, UIHelper.ValidateInput('text', 2))


if __name__ == '__main__':
    unittest.main()
