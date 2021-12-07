from utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)


def sumdiff1(count, n):
    ans = 0
    for k, v in count.items():
        ans += (abs(k - n)) * v
    return ans


def sumdiff2(count, n):
    ans = 0
    for k, v in count.items():
        df = abs(k - n)
        ans += (df * (df + 1) // 2) * v
    return ans


def part1():
    crabs = [int(x) for x in slines[0].split(",")]
    count = d()
    for c in crabs:
        count[c] += 1
    ans = 17892368127
    for i in range(min(count), max(count)):
        ans = min(ans, sumdiff1(count, i))

    return ans


def part2():
    crabs = [int(x) for x in slines[0].split(",")]
    count = d()
    for c in crabs:
        count[c] += 1
    ans = 17892368127
    for i in range(min(count), max(count)):
        ans = min(ans, sumdiff2(count, i))

    return ans


print("part1:", part1())
print("part2:", part2())
