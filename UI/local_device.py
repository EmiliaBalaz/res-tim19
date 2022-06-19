import random
import time


class LocalDevice:
    def __init__(self, type, value):
        self.type = type
        self.code = str(hash(round(random.uniform(0, 100000), 2)))
        self.timestamp = int(time.time())
        self.value = value

    def __eq__(self, other):
        if self.code == other.code:
            return True
        return False

    def __str__(self):
        return f'Local Device: Type: {self.type} Time: {self.timestamp} Value: {self.value} Code: {self.code}'
