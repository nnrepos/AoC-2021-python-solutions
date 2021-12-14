from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)


def step(a, arr):
    ins = []
    for i in range(len(a) - 1):
        pol = a[i] + a[i + 1]
        if pol in arr:
            ins.append((i, arr[pol]))

    for i, x in reversed(sorted(ins)):
        a = a[:i + 1] + x + a[i + 1:]

    return a


def step2(a, arr):
    ins = d()
    for k, v in a.items():
        if k in arr:
            k_start = k[0] + arr[k]
            k_end = arr[k] + k[1]
            ins[k_start] += v
            ins[k_end] += v
            ins[k] -= v

    for k, v in ins.items():
        a[k] += ins[k]

    return a


def part1():
    a, b = lines.split("\n\n")
    arrows = {}
    for xx in b.splitlines():
        x = xx.split()
        arrows[x[0]] = x[2]
    for i in range(10):
        a: str = step(a, arrows)

    c = Counter(a)
    return max(c.values()) - min(c.values())


def part2():
    aa, b = lines.split("\n\n")
    first, last = aa[0], aa[-1]
    arrows = {}
    for xx in b.splitlines():
        x = xx.split()
        arrows[x[0]] = x[2]

    a = d()
    for i in range(len(aa) - 1):
        a[aa[i] + aa[i + 1]] += 1

    for i in range(40):
        a: d = step2(a, arrows)

    vals = d()
    for k, v in a.items():
        vals[k[0]] += v
        vals[k[1]] += v

    vals[first] += 1
    vals[last] += 1
    for k, v in vals.items():
        assert vals[k] % 2 == 0
        vals[k] //= 2

    return max(vals.values()) - min(vals.values())


print("part1:", part1())
print("part2:", part2())
