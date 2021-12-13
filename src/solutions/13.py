from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

pp(lines)


def parse_lines():
    mp = d()
    flds = []

    lines1, lines2 = lines.split("\n\n")

    for ll in lines1.splitlines():
        x, y = ll.split(",")
        mp[(int(x), int(y))] = 1

    for ll in lines2.splitlines():
        _, _, target = ll.split()
        a, b = target.split("=")
        flds.append((a, b))

    return mp, flds


def do_fold(mp, fold):
    new_mp = d()
    yx, num = fold
    num = int(num)
    if yx == "y":
        for k, v in mp.items():
            if v > 0:
                xx, yy = k
                nyy = 2 * num - yy
                if yy >= num:
                    new_mp[(xx, nyy)] += 1
                    new_mp[k] = 0
    else:
        for k, v in mp.items():
            if v > 0:
                xx, yy = k
                nxx = 2 * num - xx
                if xx >= num:
                    new_mp[(nxx, yy)] += 1
                    new_mp[k] = 0

    for k, v in new_mp.items():
        mp[k] = v


def part1():
    mp, flds = parse_lines()
    do_fold(mp, flds[0])

    ans = 0
    for k, v in mp.items():
        if v > 0:
            ans += 1

    return ans


def part2():
    mp, flds = parse_lines()
    for fld in flds:
        do_fold(mp, fld)

    max_x = max_y = 0
    for k, v in mp.items():
        xx, yy = k
        if v > 0:
            max_x = max(max_x, xx)
            max_y = max(max_y, yy)

    print("part2:")
    for yy in range(max_y + 1):
        for xx in range(max_x + 1):
            k = (xx, yy)
            print('X' if mp[k] else '_', end='')
        print()


print("part1:", part1())
part2()  # JPZCUAUR
