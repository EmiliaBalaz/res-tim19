from UI.local_device import LocalDevice
from UI.ui_helper import UIHelper


class App:
    @staticmethod
    def Start() -> LocalDevice:
        return App.MainMenu()  # TODO: Use this value

    @staticmethod
    def MainMenu() -> LocalDevice:  # pragma: no cover
        options = ['Send local device']
        user_input = UIHelper.ShowMenu(options)
        new_local_device = None
        if user_input == 1:
            new_local_device = App.SendLocalDevice()
        return new_local_device

    @staticmethod
    def SendLocalDevice() -> LocalDevice:
        local_device_type = None
        local_device_value = None

        options = ['Digital', 'Analog']
        user_input = UIHelper.ShowMenu(options)
        if user_input == 1:
            local_device_type = 'Digital'
            local_device_value = App.SendDigitalDevice()
        elif user_input == 2:
            local_device_type = 'Analog'
            local_device_value = App.SendAnalogDevice()

        new_local_device = LocalDevice(local_device_type, local_device_value)
        return new_local_device

    @staticmethod
    def SendDigitalDevice() -> str:
        options = ['On', 'Off']
        user_input = UIHelper.ShowMenu(options)
        if user_input == 1:
            return 'On'
        elif user_input == 2:
            return 'Off'

    @staticmethod
    def SendAnalogDevice() -> int:
        while True:
            print('\nValue: ', end='')
            user_input = input()
            if UIHelper.ValidateInput(user_input, 100000):
                return int(user_input)


if __name__ == '__main__':
    App.Start()
