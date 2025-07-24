from global_variables import ZERO, ONE, TWO, X, Y, Z, BLANK
from excpetions import Accept, Reject
from tape import Tape

class ThreeTapeTuringMachine():
    def __init__(self):
        super().__init__()
        self.tape_1 = Tape("one")
        self.tape_2 = Tape("two")
        self.tape_3 = Tape("three")

    def read(self, input_string):
        try:
            self.prepare_tapes(input_string)
            self.write_numbers_on_other_tapes()
            self.go_back_tape_two_and_three()
            self.verify_if_tapes_are_the_same_size()
        except Accept:
            return True
        except Reject:
            return False
        return False 

    def get_name(self):
        return "Turing Machine (Three Tapes)"

    def last_run_steps(self):
        return self.steps_counter

    def prepare_tapes(self, input_string):
        self.steps_counter = 0
        self.tape_1.prepare(input_string)
        self.tape_2.prepare(BLANK * len(input_string))
        self.tape_3.prepare(BLANK * len(input_string))

    def write_numbers_on_other_tapes(self):
        if self.tape_1.current() == BLANK:
            raise Accept()

        self.write_zeroes_on_tape_2()
        self.write_ones_on_tape_3()

    def write_zeroes_on_tape_2(self):
        while self.tape_1.current() == ZERO:
            self.tape_2.write(ZERO)
            self.tape_2.go_right()
            self.tape_1.go_right()

            self.steps_counter += 3

        if self.tape_1.current() != ONE:
            raise Reject()

    def write_ones_on_tape_3(self):
        while self.tape_1.current() == ONE:
            self.tape_3.write(ONE)
            self.tape_3.go_right()
            self.tape_1.go_right()

            self.steps_counter += 3

        if self.tape_1.current() != TWO:
            raise Reject()

    def go_back_tape_two_and_three(self):
        self.tape_2.go_left()
        self.tape_3.go_left()
        self.steps_counter += 2

    def verify_if_tapes_are_the_same_size(self):
        while True:
            if (self.tape_1.current() == TWO and
                self.tape_2.current() == ZERO and
                self.tape_3.current() == ONE):

                self.tape_1.write(Z)
                self.tape_1.go_right()
                self.tape_2.write(X)
                self.tape_2.go_left()
                self.tape_3.write(Y)
                self.tape_3.go_left()

                self.steps_counter += 6

            elif (self.tape_1.current() == BLANK and
                  self.tape_2.current() == X and
                  self.tape_3.current() == Y):
                raise Accept()
            else:
                raise Reject()
