from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

pp(lines)
visited = d()

gr = defaultdict(lambda: [])


def numpaths(start: str):
    if start == "end":
        return 1
    elif visited[start] > 0:
        return 0
    if start.islower():
        visited[start] += 1

    ans = sum(numpaths(dest) for dest in gr[start])

    if visited[start] > 0:
        visited[start] = 0

    return ans


def numpaths2(start: str, twice):
    # note: the efficient solution is to use `twice` when reaching the visited node the *second* time.
    if start == "end":
        if visited[twice] > 1:
            return 1
        else:
            return 0
    elif visited[start] > 0:
        if start == twice and visited[start] == 1:
            pass
        else:
            return 0

    if start.islower():
        visited[start] += 1

    ans = sum(numpaths2(dest, twice) for dest in gr[start])

    if visited[start] > 0:
        visited[start] -= 1

    return ans


def part1():
    global gr
    gr = defaultdict(lambda: [])
    pairs = []

    for line in slines:
        a, b = line.split("-")
        pairs.append((a, b))
        gr[a].append(b)
        gr[b].append(a)

    return numpaths("start")


def part2():
    global gr
    gr = defaultdict(lambda: [])
    pairs = []

    for line in slines:
        a, b = line.split("-")
        pairs.append((a, b))
        gr[a].append(b)
        gr[b].append(a)

    return part1() + sum(numpaths2("start", x) for x in gr if x.islower() and x != "start")


print("part1:", part1())
print("part2:", part2())
