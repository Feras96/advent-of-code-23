import re

def find_parts_and_numbers(lines: list[str]):
    numbers = {}
    parts_indexes = {}
    for row, line in enumerate(lines):
        line = line.strip()
        part_idx = []
        num_idx = []
        num_pattern = r'\d+'
        numbers_in_row = re.findall(num_pattern, line)
        start = -1
        end = 0
        for idx, char in enumerate(line):
            if not char.isnumeric() and char != '.':
                part_idx.append(idx)
            if char.isnumeric() and start == -1:
                start = idx
                end = idx
            elif char.isnumeric():
                end = idx
            elif start != -1:
                num_idx.append((int(numbers_in_row[len(num_idx)]), start, end))
                start = -1
                end = 0
            else:
                start = -1
                end = 0
        if start != -1:
            num_idx.append((int(numbers_in_row[len(num_idx)]), start, end))
        numbers[row] = num_idx
        parts_indexes[row] = part_idx
    return numbers, parts_indexes

def is_in_range(number_pos, idx):
    if idx in range(number_pos[1] - 1, number_pos[2] + 2):
        return number_pos[0]
    else:
        return 0

def find_rel_parts(num, parts):
    sum_of_parts = 0
    for row, values in parts.items():
        for part_idx in values:
            top_matches = [is_in_range(x, part_idx) for x in num.get(row - 1, [])]
            middle_matches = [is_in_range(x, part_idx) for x in num.get(row, [])]
            bottom_matches = [is_in_range(x, part_idx) for x in num.get(row + 1, [])]
            sum_of_parts += sum(top_matches)
            sum_of_parts += sum(middle_matches)
            sum_of_parts += sum(bottom_matches)
    return sum_of_parts     

with open('input.txt', 'r') as f:
    lines = f.readlines()

num, parts = find_parts_and_numbers(lines)
print(find_rel_parts(num, parts))