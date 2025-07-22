from execution import execute_machines_with_input

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
    
    user_input = input(description)
    execute_machines_with_input(user_input)

if __name__ == "__main__":
    main()
