from execution import execute_machines_with_input

tests = [
    ("", True),
    ("012", True),
    ("001122", True),
    ("000111222", True),
    ("000011112222", True),
    ("0011122", False),
    ("000112222", False),
    ("000011222", False),
    ("122", False),
    ("112222", False),
    ("111122", False),
    ("022", False),
    ("00022", False),
    ("000222", False),
    ("0222", False),
    ("000022", False),
    ("0000222", False),
    ("01", False),
    ("00111", False),
    ("00011", False),
    ("000111", False),
    ("0111", False),
    ("0001", False),
    ("000011", False),
    ("2", False),
    ("22", False),
    ("222", False),
    ("2222", False),
    ("11", False),
    ("111", False),
    ("1111", False),
    ("0", False),
    ("0000", False),
    ("102", False),
    ("120", False),
    ("210", False),
    ("201", False),
    ("111000222", False),
    ("010101222", False),
]

for input_str, expected in tests:
    result = execute_machines_with_input(input_str)
    if result[0] != expected:
        raise Exception(f"Result: {result[0]}\Expected: {result[1]}")
    
    print(f"Input: {input_str}, expected: {expected}, got: {result[0]}")
