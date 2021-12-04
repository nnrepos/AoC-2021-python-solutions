from utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)


def board_sum(board, marks, b):
    res = 0
    for i in range(5):
        for j in range(5):
            if not marks[i][j]:
                res += board[i][j]
    return res * b


def part1():
    boards = []
    marked = []
    bingo = [int(x) for x in slines[0].split(",")]
    for i in range(2, len(slines), 6):
        index = (i - 2) // 6
        boards.append([])
        marked.append([])

        for j in range(5):
            boards[index].append([int(x) for x in slines[i + j].split()])
            marked[index].append([False] * 5)

    for b in bingo:
        for x in range(len(boards)):
            for row in range(len(boards[0])):
                for col in range(len(boards[0][0])):
                    if boards[x][row][col] == b:
                        marked[x][row][col] = True
                        if marked[x][row][0] and marked[x][row][1] and marked[x][row][2] and marked[x][row][3] and marked[x][row][4]:
                            return board_sum(boards[x], marked[x], b)
                        if marked[x][0][col] and marked[x][1][col] and marked[x][2][col] and marked[x][3][col] and marked[x][4][col]:
                            return board_sum(boards[x], marked[x], b)

    return None

def part2():
    boards = []
    marked = []
    winners = []
    bingo = [int(x) for x in slines[0].split(",")]
    for i in range(2, len(slines), 6):
        index = (i - 2) // 6
        boards.append([])
        marked.append([])
        winners.append(False)
        for j in range(5):
            boards[index].append([int(x) for x in slines[i + j].split()])
            marked[index].append([False] * 5)

    for b in bingo:
        for x in range(len(boards)):
            for row in range(len(boards[0])):
                for col in range(len(boards[0][0])):
                    if boards[x][row][col] == b:
                        marked[x][row][col] = True
                        if marked[x][row][0] and marked[x][row][1] and marked[x][row][2] and marked[x][row][3] and marked[x][row][4]:
                            winners[x] = True
                            if all(winners):
                                return board_sum(boards[x], marked[x], b)
                        if marked[x][0][col] and marked[x][1][col] and marked[x][2][col] and marked[x][3][col] and marked[x][4][col]:
                            winners[x] = True
                            if all(winners):
                                return board_sum(boards[x], marked[x], b)

    return None


print("part1:", part1())
print("part2:", part2())
