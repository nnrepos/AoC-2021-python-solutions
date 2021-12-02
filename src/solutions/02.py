from utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()


def part1():
    forw = 0
    down = 0
    for line in slines:
        x, y = line.split()
        if x == "forward":
            forw += int(y)
        if x == "down":
            down += int(y)
        if x == "up":
            down -= int(y)
    return forw * down


def part2():
    forw = 0
    down = 0
    aim = 0
    for line in slines:
        x, y = line.split()
        y = int(y)
        if x == "forward":
            forw += y
            down += y * aim
        if x == "down":
            aim += y
        if x == "up":
            aim -= y
    return forw * down


print("part1:", part1())
print("part2:", part2())
