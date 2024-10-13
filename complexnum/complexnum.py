import typing
from tokenizer import ConvertToToken


class ComplexNum:
    def __init__(self, *constants):
        self.constants = constants
        self.variables = {}

    def set_var(self, var, *values):
        try:
            self.variables[var] = values
        except KeyError:
            raise ValueError(f"Variable {var} already exists.")
        except Exception as e:
            raise ValueError(f"Assigning error: {e}")

    def solve(self, equation):
        tokens = ConvertToToken(
            ["+", "-", "*", "/"], equation, ["+", "-", "*", "/"], ["+", "-", "*", "/"]
        )
        tokenized_output, tokenized_dict, tokenized_output_w_spaces = tokens.tokenize()
        for j, i in enumerate(tokenized_output):
            if i in self.variables:
                tokenized_output[j] = str(self.variables[i][0][0])
        print(eval(str("".join(tokenized_output))))


myvalues = ComplexNum(1, 2, 3)
myvalues.set_var("a", [1])
myvalues.set_var("b", [4])
myvalues.set_var("c", [3])

myvalues.solve("a - (b - c)")
