from src.utils.utils import *

pp = print

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)


def part1():
    ans = 0
    for line in slines:
        for c in line.split("|")[1].split():
            if len(c) in (2, 3, 4, 7):
                ans += 1
    return ans


def part2():
    ans = 0
    for line in slines:
        num_dict = {}
        a, b = line.split("|")
        for c in a.split(" "):
            c = set(sorted(c))
            if len(c) == 2:
                num_dict[1] = c
            elif len(c) == 3:
                num_dict[7] = c
            elif len(c) == 4:
                num_dict[4] = c
            elif len(c) == 7:
                num_dict[8] = c
        num_dict["top"] = num_dict[7] - num_dict[1]
        for c in a.split(" "):
            c = set(sorted(c))
            if len(c) == 5:
                if num_dict[1].issubset(c):
                    num_dict[3] = c
        for c in a.split(" "):
            c = set(sorted(c))
            if len(c) == 6:
                if num_dict[3].issubset(c):
                    num_dict[9] = c
        num_dict["bottom_left"] = num_dict[8] - num_dict[9]
        for c in a.split(" "):
            c = set(sorted(c))
            if len(c) == 5 and c != num_dict[3]:
                if num_dict["bottom_left"].issubset(c):
                    num_dict[2] = c
                else:
                    num_dict[5] = c
        for c in a.split(" "):
            c = set(sorted(c))
            if len(c) == 6 and c != num_dict[9]:
                if num_dict[5].issubset(c):
                    num_dict[6] = c
                else:
                    num_dict[0] = c
        curr = ""
        for c in b.split(" "):
            c = set(sorted(c))
            for k, v in num_dict.items():
                if v == c:
                    curr += str(k)
        ans += int(curr)

    return ans


print("part1:", part1())
print("part2:", part2())
