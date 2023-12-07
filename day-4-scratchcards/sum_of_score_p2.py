# The number of cards is equal to current number of current card (starting with 1 each)
# Then we update the number of occurances of the following cards if we win by the number of
# occurances of the current card.


def get_matches(line: str):
    split_line = line.split(':')
    card_number = int(''.join(split_line[0][5:]))
    clean_line = split_line[1]
    number_line = clean_line.split('|')
    winning_numbers = set([num.strip() for num in number_line[0].split(' ') if num != ''])
    selected_numbers = [num.strip() for num in number_line[1].split(' ') if num != '']
    matches = [num for num in selected_numbers if num in winning_numbers]
    return len(matches)

with open('input.txt', 'r') as f:
    lines = f.readlines()

count = [1] * len(lines)
for line_num, line in enumerate(lines):
    for i in range(get_matches(line)):
        count[line_num + i + 1] = count[line_num + i + 1] + count[line_num]

print(sum(count))