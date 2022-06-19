import unittest
from unittest.mock import patch

from UI.local_device import LocalDevice
from UI.local_device_ui import App


class TestUIHelper(unittest.TestCase):
    @patch('builtins.input', return_value=100)
    def test_send_local_device(self, input):
        with patch('local_device_ui.UIHelper.ShowMenu', return_value=1):
            actual_local_device = App.SendLocalDevice()
            expected_local_device = LocalDevice('Digital', 'On')
            self.assertEqual(expected_local_device.type, actual_local_device.type)
            self.assertEqual(expected_local_device.value, actual_local_device.value)

        with patch('local_device_ui.UIHelper.ShowMenu', return_value=2):
            actual_local_device = App.SendLocalDevice()
            expected_local_device = LocalDevice('Analog', 100)
            self.assertEqual(expected_local_device.type, actual_local_device.type)
            self.assertEqual(expected_local_device.value, actual_local_device.value)

    def test_send_digital_device(self):
        with patch('local_device_ui.UIHelper.ShowMenu', return_value=1):
            self.assertEqual('On', App.SendDigitalDevice())

        with patch('local_device_ui.UIHelper.ShowMenu', return_value=2):
            self.assertEqual('Off', App.SendDigitalDevice())

    @patch('builtins.input', return_value='100')
    def test_send_analog_device(self, input):
        self.assertEqual(100, App.SendAnalogDevice())


if __name__ == '__main__':
    unittest.main()
