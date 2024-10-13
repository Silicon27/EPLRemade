"""
By linking the Output class with the nodes of the Board class, we can create a circuit board that can be used to simulate circuits.
"""

import os


class Output:
    def __init__(self, value: bool = False):
        self.value = value

    def get_value(self):
        return self.value


class Board:
    def __init__(self, output: Output = Output(), displayonchange: bool = True):
        self.output = output
        self.value = output.get_value()
        self.lastop = "\033[36mASSIGNED\033[0m"
        self.displayonchange = displayonchange

    def NOT(self):
        self.value = not self.output.get_value()
        self.lastop = "\033[92mNOT\033[0m"
        if self.displayonchange:
            self.display()

    def OR(self, *inputs):
        self.value = any(inputs)
        self.lastop = "\033[93mOR\033[0m"
        if self.displayonchange:
            self.display()

    def AND(self, *inputs):
        self.value = all(inputs)
        self.lastop = "\033[94mAND\033[0m"
        if self.displayonchange:
            self.display()

    def XOR(self, *inputs):
        if all(inputs) or not any(inputs):
            self.value = False
        else:
            self.value = True
        self.lastop = "\033[95mXOR\033[0m"
        if self.displayonchange:
            self.display()

    def NAND(self, *inputs):
        self.value = not all(inputs)
        self.lastop = "\033[96mNAND\033[0m"
        if self.displayonchange:
            self.display()

    def display(self):
        if self.value:
            print(
                f"{self.value}:  [\033[42m \033[0m]            last operation: {self.lastop}"
            )
        else:
            print(
                f"{self.value}: [\033[41m \033[0m]            last operation: {self.lastop}"
            )


# Test them
board = Board(Output(True), displayonchange=True)
board.display()
board.NOT()  # False
board.OR(True, False)  # True
board.OR(False, False)  # False
board.OR(False, True)  # True
board.AND(True, False)  # False
board.AND(True, True)  # True
board.XOR(True, False)  # True
board.XOR(True, True)  # False
board.NAND(True, False)  # True
board.NAND(True, True)  # False
