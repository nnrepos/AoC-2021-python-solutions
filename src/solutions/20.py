from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

trans = []

tr, gr = lines.split("\n\n")
tr, gr = tr.strip(), [ll.strip() for ll in gr.strip().splitlines()]

for pix in tr:
    if pix == '#':
        trans.append(1)
    elif pix == '.':
        trans.append(0)
    else:
        assert False

NEI = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def part1():
    grid = d()
    for i, r in enumerate(gr):
        for j, pixel in enumerate(r):
            if pixel == '#':
                grid[(i, j)] = 1
            elif pixel == '.':
                grid[(i, j)] = 0
            else:
                assert False

    start = (min(min([key[0] for key in grid]), min([key[1] for key in grid]))) - 5
    end = (max(max([key[0] for key in grid]), max([key[1] for key in grid]))) + 5
    for step in range(2):
        new_grid = d()
        other_pixels = step % 2
        for row in range(start, end + 1):
            for col in range(start, end + 1):
                for ii, (drow, dcol) in enumerate(NEI):
                    if row + drow in range(start, end) and col + dcol in range(start, end):
                        new_grid[(row, col)] += grid[(row + drow, col + dcol)] << (8 - ii)
                    else:
                        new_grid[(row, col)] += other_pixels << (8 - ii)

                new_grid[(row, col)] = trans[new_grid[(row, col)]]
        grid = new_grid

    c = Counter(grid.values())
    ans = c[1]
    return ans


def print_grid(grid, start, end):
    print()
    for row in range(start, end):
        for col in range(start, end):
            if grid[(row, col)] == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()


def part2():
    grid = d()
    for i, r in enumerate(gr):
        for j, pixel in enumerate(r):
            if pixel == '#':
                grid[(i, j)] = 1
            elif pixel == '.':
                grid[(i, j)] = 0
            else:
                assert False

    start = (min(min([key[0] for key in grid]), min([key[1] for key in grid]))) - 55
    end = (max(max([key[0] for key in grid]), max([key[1] for key in grid]))) + 55
    print('this takes a while')
    for step in range(50):
        print(step)
        # print_grid(grid, start, end)
        new_grid = d()
        other_pixels = step % 2

        for row in range(start, end):
            for col in range(start, end):
                for ii, (drow, dcol) in enumerate(NEI):
                    if row + drow in range(start, end) and col + dcol in range(start, end):
                        new_grid[(row, col)] += grid[(row + drow, col + dcol)] << (8 - ii)
                    else:
                        new_grid[(row, col)] += other_pixels << (8 - ii)

                new_grid[(row, col)] = trans[new_grid[(row, col)]]
        grid = new_grid

    c = Counter(grid.values())
    ans = c[1]
    return ans


print("part1:", part1())
print("part2:", part2())
