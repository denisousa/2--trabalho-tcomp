from global_variables import BLANK, NUMBER_OF_BLANKS_AFTER

class Tape:
    def __init__(self):
        self.tape = []
        self.cursor = 0

    def prepare(self, input_string):
        self.reset()
        self.tape = list(input_string) + [BLANK] * NUMBER_OF_BLANKS_AFTER

    def go_left(self):
        if self.cursor > 0:
            self.cursor -= 1

    def go_right(self):
        if self.cursor < len(self.tape) - 1:
            self.cursor += 1

    def write(self, char):
        self.tape[self.cursor] = char

    def reset(self):
        self.cursor = 0
        self.tape.clear()

    def current(self):
        return self.tape[self.cursor]
