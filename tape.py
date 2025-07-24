from global_variables import BLANK, SHOW_STEPS, SHOW_WRITE, SHOW_PREPARE

class Tape:
    def __init__(self, name):
        self.tape = []
        self.cursor = 0
        self.name = name

    def prepare(self, input_string):
        self.tape = list(input_string) + [BLANK]
        if SHOW_PREPARE:
            print(' '.join(self.tape) + f'  {self.name}  prepare')
            print('  ' * self.cursor + '^')

    def go_left(self):
        if self.cursor > 0:
            self.cursor -= 1
            if SHOW_STEPS:
                print(' '.join(self.tape) + f'  {self.name}')
                print('  ' * self.cursor + '^')

    def go_right(self):
        if self.cursor < len(self.tape) - 1:
            self.cursor += 1
            if SHOW_STEPS:
                print(' '.join(self.tape) + f'  {self.name}')
                print('  ' * self.cursor + '^')

    def write(self, char):
        self.tape[self.cursor] = char
        if SHOW_WRITE:
            print(' '.join(self.tape) + f'  {self.name}')
            print('  ' * self.cursor + '^')

    def current(self):
        return self.tape[self.cursor]
