from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)
RANGE_START = 1111_1111_1111_11


def parse_in():
    return [x.split() for x in slines]


cmdlist = parse_in()
regs = d()
inputs_index = 0


def step(inputs, cmd, arg1, arg2=None, arg3=None):
    global inputs_index
    val2 = None
    if arg2 is not None:
        try:
            arg2 = int(arg2)
            val2 = arg2
        except ValueError:
            val2 = regs[arg2]
    try:
        if cmd == "inp":
            assert arg2 is None
            regs[arg1] = int(inputs[inputs_index])
            inputs_index += 1
        elif cmd == "add":
            assert arg2 is not None
            regs[arg1] = regs[arg1] + val2
        elif cmd == "mul":
            assert arg2 is not None
            regs[arg1] = regs[arg1] * val2
        elif cmd == "div":
            assert arg2 is not None
            regs[arg1] = regs[arg1] // val2
        elif cmd == "mod":
            assert arg2 is not None
            regs[arg1] = regs[arg1] % val2
        elif cmd == "eql":
            assert arg2 is not None
            regs[arg1] = 1 if (regs[arg1] == val2) else 0
        elif cmd == "addmod":
            a1, a2, a3 = int(arg1), int(arg2), int(arg3)
            inn = int(inputs[inputs_index])
            inputs_index += 1

            regs['z'] //= a1
            mod26 = regs['z'] % 26
            # try inn+a3 = rev(a2) mod26
            inn = 0
            pp(f"{mod26=},{a2=},{inn=}")
            regs['z'] *= (1 if (((regs['z'] % 26) + a2) == inn) else 26)
            regs['z'] += (inn+a3) * ((regs['z'] % 26) + a2)
            pp(regs['z'])
        else:
            assert False
    except Exception as e:
        return e


def is_legal(inputs):
    global regs
    global inputs_index
    inputs_index = 0
    regs = d()

    for cmdl in cmdlist:
        e = step(inputs, *cmdl)
        if e:
            pp(e)
            break
    else:
        if regs['z'] == 0:
            return True
    return False


def part1():
    global cmdlist
    newcmdlist = []

    add25_1 = [
        ['eql', 'x', 'w'],
        ['eql', 'x', '0'],
        ['mul', 'y', '0'],
        ['add', 'y', '25'],
        ['mul', 'y', 'x'],
        ['add', 'y', '1'],
        ['mul', 'z', 'y'],
        ['mul', 'y', '0'],
        ['add', 'y', 'w'],
    ]

    mod26_1 = [
        ['inp', 'w'],
        ['mul', 'x', '0'],
        ['add', 'x', 'z'],
        ['mod', 'x', '26']
    ]
    l25 = len(add25_1)
    l26 = len(mod26_1)

    i = 0
    while i < len(cmdlist):
        if (i + l25 + 2 < len(cmdlist) and cmdlist[i:i + l25] == add25_1 and
                cmdlist[i + l25][0] == 'add' and cmdlist[i + l25][1] == 'y' and
                cmdlist[i + l25 + 1] == ['mul', 'y', 'x'] and
                cmdlist[i + l25 + 2] == ['add', 'z', 'y']):
            newcmdlist.append(['add25', cmdlist[i + l25][2]])
            i += l25 + 3
        elif (i + l26 + 1 < len(cmdlist) and cmdlist[i:i + l26] == mod26_1 and
              cmdlist[i + l26][0] == 'div' and cmdlist[i + l26][1] == 'z' and
              cmdlist[i + l26 + 1][0] == 'add' and cmdlist[i + l26 + 1][1] == 'x'):
            newcmdlist.append(['mod26', cmdlist[i + l26][2], cmdlist[i + l26 + 1][2]])
            i += l26 + 2
        else:
            newcmdlist.append(cmdlist[i])
            i += 1
    cmdlist = newcmdlist

    i = 0
    newcmdlist = []
    while i < len(cmdlist):
        if i + 1 < len(cmdlist) and cmdlist[i][0] == 'mod26' and cmdlist[i + 1][0] == 'add25':
            newcmdlist.append(['addmod', cmdlist[i][1], cmdlist[i][2], cmdlist[i + 1][1]])
            i += 2
        else:
            newcmdlist.append(cmdlist[i])
            i += 1
    cmdlist = newcmdlist

    # for cmdl in cmdlist:
    #     pp(cmdl)

    for i in range(RANGE_START, RANGE_START + 1000):
        if '0' in str(i):
            continue

        if is_legal(str(i)):
            print('legal', i)


def part2():
    return


print("part1:", part1())
print("part2:", part2())
