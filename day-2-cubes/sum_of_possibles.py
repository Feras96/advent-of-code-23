import re

def check_if_possible(game_line: str, red_cubes: int, green_cubes: int, blue_cubes: int) -> bool:
    pattern = r'(\d+)\s(red|green|blue)'
    matches = re.findall(pattern, game_line)
    reds = [int(cubes[0]) for cubes in matches if cubes[1] == 'red']
    greens = [int(cubes[0]) for cubes in matches if cubes[1] == 'green']
    blues = [int(cubes[0]) for cubes in matches if cubes[1] == 'blue']

    return max(reds) <= red_cubes and max(greens) <= green_cubes and max(blues) <= blue_cubes

with open('input.txt', 'r') as f:
    lines = f.readlines()
sum_of_possible_ids = 0
for idx, line in enumerate(lines):
    if check_if_possible(line, 12, 13, 14):
        sum_of_possible_ids += idx + 1
print(sum_of_possible_ids)