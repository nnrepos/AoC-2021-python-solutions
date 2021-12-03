from utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
lines_as_nums = lines_to_nums(lines)


def part1():
    x = ""
    y = ""
    lenline = len(slines[0])
    common_bits = lenline * [0]
    nlines = len(slines)

    # find most common bits in each index
    for line in slines:
        for i in range(lenline):
            common_bits[i] += int(line[i])

    # build the binary numbers based on common bit
    for i in range(lenline):
        m = 0
        if common_bits[i] > (nlines / 2):
            m = 1
        x += str(m)
        y += str(1 - m)

    x = int(x, 2)
    y = int(y, 2)
    return x * y


def part2():
    xlines = slines
    ylines = slines
    lenline = len(xlines[0])

    for i in range(lenline):
        common_bits1 = lenline * [0]
        common_bits2 = lenline * [0]
        for line in xlines:
            for j in range(lenline):
                common_bits1[j] += int(line[j])

        for line in ylines:
            for j in range(lenline):
                common_bits2[j] += int(line[j])

        # filter lines according to most common bit. stop if 1 remaining.
        if len(xlines) > 1:
            if common_bits1[i] >= len(xlines) / 2:
                xlines = [xl for xl in xlines if xl[i] == "1"]
            else:
                xlines = [xl for xl in xlines if xl[i] == "0"]

        if len(ylines) > 1:
            if common_bits2[i] < len(ylines) / 2:
                ylines = [yl for yl in ylines if yl[i] == "1"]
            else:
                ylines = [yl for yl in ylines if yl[i] == "0"]

    x = int(xlines[0], 2)
    y = int(ylines[0], 2)

    return x * y


print("part1:", part1())
print("part2:", part2())
