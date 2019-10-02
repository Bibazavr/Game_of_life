f = open('input.txt', 'r')
first_stage = []
row, column = 5, 5
for line in f:
    first_stage.append(line.split())

next_stage = []


def find_live(stage, row, elem,):
    live = 0
    for i in stage:
        print(i)
    print(elem)
    if stage[-row + 1][elem] == 'x':
        live += 1
    if stage[-row - 1][elem] == 'x':
        live += 1
    if stage[-row][elem - 1] == 'x':
        live += 1
    if stage[-row][elem + 1] == 'x':
        live += 1
    return live


for i in range(row):
    next_row = []
    for j in range(column):
        count_live = find_live(first_stage, i, j)
        print(count_live)
        if first_stage[i][j] == 'x' and 2 < count_live <= 3:
            next_stage.append(i)

    next_stage.append(next_row)

for row in next_stage:
    for j in row:
        print(j)
