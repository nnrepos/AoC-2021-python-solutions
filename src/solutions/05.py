from utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)


def part1():
    coords = []
    for line in slines:
        p1, p2 = line.split("->")
        x1, y1 = [int(z) for z in p1.split(",")]
        x2, y2 = [int(z) for z in p2.split(",")]
        coords.append([x1, y1, x2, y2])

    max_coord = 0
    for cs in coords:
        for c in cs:
            max_coord = max(max_coord, c)
    max_coord += 1

    board = [[0] * max_coord for _ in range(max_coord)]

    for x1, y1, x2, y2 in coords:
        if x1 == x2:
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            for yy in range(ymin, ymax + 1):
                board[x1][yy] += 1
        elif y1 == y2:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            for xx in range(xmin, xmax + 1):
                board[xx][y1] += 1

    ans = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] > 1:
                ans += 1

    return ans


def part2():
    coords = []
    for line in slines:
        p1, p2 = line.split("->")
        x1, y1 = [int(z) for z in p1.split(",")]
        x2, y2 = [int(z) for z in p2.split(",")]
        coords.append([x1, y1, x2, y2])

    max_coord = 0
    for cs in coords:
        for c in cs:
            max_coord = max(max_coord, c)
    max_coord += 1

    board = [[0] * max_coord for _ in range(max_coord)]

    for x1, y1, x2, y2 in coords:
        if x1 == x2:
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            for yy in range(ymin, ymax + 1):
                board[x1][yy] += 1
        elif y1 == y2:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            for xx in range(xmin, xmax + 1):
                board[xx][y1] += 1
        else:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            if (y1 > y2 and x1 > x2) or (y1 < y2 and x1 < x2):
                for i in range(xmax + 1 - xmin):
                    board[xmin + i][ymin + i] += 1
            else:
                for i in range(xmax + 1 - xmin):
                    board[xmin + i][ymax - i] += 1

    ans = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] > 1:
                ans += 1

    return ans


print("part1:", part1())
print("part2:", part2())
