from src.utils.utils import *
from copy import deepcopy

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

mm = []
for line in slines:
    mm.append([x for x in line.strip()])

rows = len(mm)
cols = len(mm[0])


def is_legal(row, col):
    return mm[row % rows][col % cols] == '.'


def step():
    global mm
    is_moved = False

    # move east
    new_mm = deepcopy(mm)
    for row in range(rows):
        for col in range(cols):
            if mm[row][col] == '>':
                if is_legal(row, col + 1):
                    new_mm[row][(col + 1) % cols] = '>'
                    new_mm[row][col] = '.'
                    is_moved = True

    mm = deepcopy(new_mm)

    # move south
    for row in range(rows):
        for col in range(cols):
            if mm[row][col] == 'v':
                if is_legal(row + 1, col):
                    new_mm[(row + 1) % rows][col] = 'v'
                    new_mm[row][col] = '.'
                    is_moved = True

    mm = deepcopy(new_mm)

    return is_moved


def draw_mm():
    print()
    print()
    for i in range(rows):
        for j in range(cols):
            print(mm[i][j], end='')
        print()


def part1():
    s = 0
    is_moved = True
    while is_moved:
        is_moved = step()
        s += 1
    return s


def part2():
    return


print("part1:", part1())
print("part2:", part2())
