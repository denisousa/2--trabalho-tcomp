from one_tape_turing_machine import OneTapeTuringMachine
from three_tape_turing_machine import ThreeTapeTuringMachine

def execute_machines_with_input(input_string):
    one_tape = OneTapeTuringMachine()
    three_tape = ThreeTapeTuringMachine()

    machines = [one_tape, three_tape]

    result = []
    print(f"Testing input '{input_string}'\n")

    for machine in machines:
        print("=" * 40)
        print(machine.get_name())

        result.append(machine.test_string(input_string))

        print("Result:", "ACCEPT" if result[-1] else "REJECT")
        print(f"Nº steps: {machine.last_run_steps()}\n")

    if 'ACCPET' in result and 'REJECT' in result:
        raise Exception(f"Result One Tape Turing Machine: {result[0]}\nResult One Three Turing Machine: {result[1]}")

    return result
