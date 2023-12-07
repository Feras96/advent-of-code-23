import re

def get_calibration_value(line: str) -> int:
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    matches = re.findall(pattern, line)
    first_digit = matches[0]
    last_digit = matches[-1]
    digit_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    first_digit = digit_map.get(first_digit, first_digit)
    last_digit = digit_map.get(last_digit, last_digit)
    return int(first_digit) * 10 + int(last_digit)

with open('input.txt', 'r') as f:
    lines = f.readlines()
sum_of_vals = 0
for line in lines:
    sum_of_vals += get_calibration_value(line)
print(sum_of_vals)
