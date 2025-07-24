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

        result.append(machine.read(input_string))

        print("\nResult:", "ACCEPT" if result[-1] else "REJECT")
        print(f"Nº steps: {machine.last_run_steps()}\n")

    if 'ACCPET' in result and 'REJECT' in result:
        raise Exception(f"Result One Tape Turing Machine: {result[0]}\nResult One Three Turing Machine: {result[1]}")

    return result



def main():

    description = """
    🧠 Turing Machine for Recognizing the Language 0^k1^k2^k, where k ≥ 0

    ✅ Valid examples:
    - For k = 0: "" (the empty string)
    - For k = 1: "012"
    - For k = 2: "001122"
    - And so on...

    ❌ Invalid examples:
    - "00112"   → the number of 2s is incorrect.
    - "0122"    → the number of 2s is greater than the number of 0s or 1s.
    - "120"     → incorrect order of symbols.

    Now write a example:
    """
    
    # user_input = input(description)
    user_input = "000111222"
    execute_machines_with_input(user_input)

if __name__ == "__main__":
    main()
