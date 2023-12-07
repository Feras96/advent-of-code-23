def get_score(line: str) -> int:
    clean_line = line.split(':')[1]
    number_line = clean_line.split('|')
    winning_numbers = set([num.strip() for num in number_line[0].split(' ') if num != ''])
    selected_numbers = [num.strip() for num in number_line[1].split(' ') if num != '']
    matches = [num for num in selected_numbers if num in winning_numbers]
    if matches:
        return 2 ** (len(matches) - 1)
    else:
        return 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

scores = []
for line in lines:
    scores.append(get_score(line))
print(sum(scores))

