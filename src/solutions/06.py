from utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

print(lines)


def part1():
    fish = [int(x) for x in lines.split(",")]
    for i in range(80):
        new_fish = []
        for f in range(len(fish)):
            if fish[f] == 0:
                fish[f] = 6
                new_fish.append(8)
            else:
                fish[f] -= 1
        fish += new_fish
    return len(fish)


def part2():
    fish = dict()
    for i in range(9):
        fish[i] = len([int(x) for x in lines.split(",") if int(x) == i])
    for i in range(256):
        new_fish = {}
        for j in range(1, 9):
            new_fish[j - 1] = fish[j]
        new_fish[8] = fish[0]
        new_fish[6] += fish[0]
        for j in range(9):
            fish[j] = new_fish[j]

    ans = 0
    for i in range(9):
        ans += fish[i]
    return ans


print("part1:", part1())
print("part2:", part2())
