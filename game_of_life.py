f = open('input.txt', 'r')
first_stage = []
row, column = 5, 5
for line in f:
    first_stage.append(list(''.join(line.split())))

next_stage = []
print('first_stage')
for i in first_stage:
    print(i)


def find_live(stage, number_row, number_column, max_row, max_column):
    live = 0
    up = number_row + 1
    right = number_column + 1

    if up > max_row-1:
        up = 0
    if right > max_column-1:
        right = 0

    if stage[up][right] == 'X':
        live += 1
    if stage[up][number_column] == 'X':
        live += 1
    if stage[up][number_column - 1] == 'X':
        live += 1
    if stage[number_row][right] == 'X':
        live += 1
    if stage[number_row][number_column - 1] == 'X':
        live += 1
    if stage[number_row - 1][right] == 'X':
        live += 1
    if stage[number_row - 1][number_column] == 'X':
        live += 1
    if stage[number_row - 1][number_column - 1] == 'X':
        live += 1
    return live


for i in range(row):
    next_row = []
    for j in range(column):
        count_live = find_live(first_stage, i, j, row, column)
        print(count_live, end=' ')
        if (first_stage[i][j] == 'X' and 2 <= count_live <= 3) or (first_stage[i][j] == '.' and count_live == 3):
            next_row.append("X")
        else:
            next_row.append('.')

    next_stage.append(next_row)

print('next_stage')
for row in next_stage:
    for item in row:
        print(item, end='')
    print()
