class UIHelper:
    @staticmethod
    def ShowMenu(options: list[str]) -> int:
        while True:
            print('\n')
            index = 0
            for option in options:
                index += 1
                print(f'{index}. {option}')
            choice = input()
            if UIHelper.ValidateInput(choice, index):
                return int(choice)

    @staticmethod
    def ValidateInput(input: str, option_count: int) -> bool:
        try:
            if 1 <= int(input) <= option_count:
                return True
            return False
        except:
            return False
