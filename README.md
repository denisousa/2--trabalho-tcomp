# Turing Machine: $0^k 1^k 2^k \quad (k \geq 0)$

This project implements two Turing Machines in Python to recognize strings of the form:

**L = { 0^k 1^k 2^k | k ≥ 0 }**

Examples:
- Valid: `""`, `"012"`, `"001122"`, `"000111222"`
- Invalid: `"00112"`, `"0112"`, `"000111"`

## Files
- `main.py`: Entry point and logic to execute the two machines
- `one_tape_turing_machine.py`: One-tape Turing Machine
- `three_tape_turing_machine.py`: Three-tape Turing Machine
- `tape.py`: Tape implementation
- `global_variables.py`: Symbol/constants
- `exceptions.py`: Accept/Reject control basesd in exceptions
- `README.md`: Documentation

## Requirements
- Python 3.7+
- No external libraries

## Usage

Run with a user input:

```python
python main.py
```

Running a previously created test suite:
```python
python tests.py
```



