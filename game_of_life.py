class GameOfLive:
    def __init__(self):
        row = self.row
        column = self.column
        next_stage = self.next_stage
        stage = self.stage

    def find_live(self, stage, number_row, number_column, max_row, max_column):
        live = 0
        up = number_row + 1
        right = number_column + 1

        if up > max_row - 1:
            up = 0
        if right > max_column - 1:
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

    def life(self, max_row, max_column, stage):
        self.stage = stage
        self.next_stage = []
        for i in range(max_row):
            next_row = []
            for j in range(max_column):
                count_live = self.find_live(stage, i, j, max_row, max_column)
                if (first_stage[i][j] == 'X' and 2 <= count_live <= 3) or (
                        first_stage[i][j] == '.' and count_live == 3):
                    next_row.append("X")
                else:
                    next_row.append('.')

            self.next_stage.append(next_row)

        print('next_stage')
        for row in self.next_stage:
            for item in row:
                print(item, end='')
            print()
        return self.next_stage

    def until_dead(self):
        while self.next_stage != self.stage:
            self.life(max_row, max_column, self.next_stage)


if __name__ == '__main__':
    row, column = 5, 5
    first_stage = []
    f = open('input.txt', 'r')
    for line in f:
        first_stage.append(list(''.join(line.split())))
    biba = GameOfLive()
    stage = biba.life(row, column, first_stage)
    while True:
        biba.life(row, column, stage)
