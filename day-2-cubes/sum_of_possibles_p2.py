import re

def get_min_possible_cubes(game_line: str) -> bool:
    pattern = r'(\d+)\s(red|green|blue)'
    matches = re.findall(pattern, game_line)
    reds = [int(cubes[0]) for cubes in matches if cubes[1] == 'red']
    greens = [int(cubes[0]) for cubes in matches if cubes[1] == 'green']
    blues = [int(cubes[0]) for cubes in matches if cubes[1] == 'blue']

    return max(reds), max(greens), max(blues)

with open('input.txt', 'r') as f:
    lines = f.readlines()
sum_of_powers = 0
for line in lines:
    reds, greens, blues = get_min_possible_cubes(line)
    sum_of_powers +=  reds * greens * blues
print(sum_of_powers)