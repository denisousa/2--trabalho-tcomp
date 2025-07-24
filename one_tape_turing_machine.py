from global_variables import ZERO, ONE, TWO, X, Y, Z, BLANK
from excpetions import Accept, Reject
from tape import Tape

class OneTapeTuringMachine():
    def __init__(self):
        super().__init__()
        self.steps_counter = 0
        self.tape = Tape("one")

    def read(self, input_string):
        try:
            self.prepare_tape(input_string)
            self.string_validation()
        except Accept:
            return True
        except Reject:
            return False
        return False 

    def string_validation(self):
        while True:
            if self.tape.current() == BLANK:
                raise Accept()
            elif self.tape.current() == ZERO:
                self.mark_x()
                self.go_right()
                self.search_for_one()
            elif self.tape.current() == Y:
                self.search_for_numbers()
            else:
                raise Reject()

    def search_for_one(self):
        while True:
            if self.tape.current() == ONE:
                self.mark_y()
                self.go_right()
                self.search_for_two()
                break
            elif self.tape.current() in (ZERO, Y):
                self.go_right()
            else:
                raise Reject()

    def search_for_two(self):
        while True:
            if self.tape.current() == TWO:
                self.mark_z()
                self.go_back()
                break
            elif self.tape.current() in (ONE, Z):
                self.go_right()
            else:
                raise Reject()

    def go_back(self):
        while self.tape.current() != X:
            self.go_left()
        self.go_right()

    def search_for_numbers(self):
        while True:
            if self.tape.current() in (Y, Z):
                self.go_right()
            elif self.tape.current() == BLANK:
                raise Accept()
            else:
                raise Reject()

    def get_name(self):
        return "Turing Machine (One Tape)"

    def prepare_tape(self, input_string):
        self.steps_counter = 0
        self.tape.prepare(input_string)

    def mark_x(self):
        self.steps_counter += 1
        self.tape.write(X)

    def mark_y(self):
        self.steps_counter += 1
        self.tape.write(Y)

    def mark_z(self):
        self.steps_counter += 1
        self.tape.write(Z)

    def go_left(self):
        self.steps_counter += 1
        self.tape.go_left()

    def go_right(self):
        self.steps_counter += 1
        self.tape.go_right()

    def last_run_steps(self):
        return self.steps_counter
