from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)


def part1():
    s = 0
    for line in slines:
        dd = deque()
        for c in line:
            if c in ("(", "[", "{", "<"):
                dd.append(c)
            else:
                ope = dd.pop()
                if (ope == '(' and c == ')' or
                        ope == '[' and c == ']' or
                        ope == '{' and c == '}' or
                        ope == '<' and c == '>'):
                    pass
                else:
                    if c == ')':
                        s += 3
                    elif c == ']':
                        s += 57
                    elif c == '}':
                        s += 1197
                    else:
                        s += 25137
                    break

    return s


def part2():
    ss = []
    for line in slines:
        s = 0
        dd = deque()
        corrupt = False
        for c in line:
            if c in ("(", "[", "{", "<"):
                dd.append(c)
            else:
                ope = dd.pop()
                if (ope == '(' and c == ')' or
                        ope == '[' and c == ']' or
                        ope == '{' and c == '}' or
                        ope == '<' and c == '>'):
                    pass
                else:
                    if c == ')':
                        s += 3
                    elif c == ']':
                        s += 57
                    elif c == '}':
                        s += 1197
                    else:
                        s += 25137
                    corrupt = True
                    break
        if corrupt:
            pass
        else:
            while len(dd) > 0:
                c = dd.pop()
                if c == '(':
                    s = s * 5 + 1
                elif c == '[':
                    s = s * 5 + 2
                elif c == '{':
                    s = s * 5 + 3
                else:
                    s = s * 5 + 4
            ss.append(s)
    return sorted(ss)[len(ss) // 2]


print("part1:", part1())
print("part2:", part2())
