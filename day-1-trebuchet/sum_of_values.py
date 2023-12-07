def get_calibration_value(line: str) -> int:
    first_digit = None
    last_digit = None
    for char in line:
        if not first_digit and char.isnumeric():
            first_digit = char
            last_digit = char
        elif first_digit and char.isnumeric():
            last_digit = char
    return int(first_digit) * 10 + int(last_digit)

with open('input.txt', 'r') as f:
    lines = f.readlines()
sum_of_vals = 0
for line in lines:
    sum_of_vals += get_calibration_value(line)
print(sum_of_vals)
