from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)

s = "".join([bin(int(b, 16))[2:].zfill(4) for b in lines.strip()])
si = 0
versions = 0


def oper(kind, packet):
    sub_packets = packet["packets"]
    if kind == 0:
        val = sum(p["val"] for p in sub_packets)
    elif kind == 1:
        val = reduce(lambda a, b: a * b, [p["val"] for p in sub_packets])
    elif kind == 2:
        val = reduce(lambda a, b: min(a, b), [p["val"] for p in sub_packets])
    elif kind == 3:
        val = reduce(lambda a, b: max(a, b), [p["val"] for p in sub_packets])
    elif kind == 5:
        val = 1 if sub_packets[0]["val"] > sub_packets[1]["val"] else 0
    elif kind == 6:
        val = 1 if sub_packets[0]["val"] < sub_packets[1]["val"] else 0
    elif kind == 7:
        val = 1 if sub_packets[0]["val"] == sub_packets[1]["val"] else 0
    else:
        assert False

    return val


def gets(leng, typ="int"):
    global si
    si += leng
    if typ == "str":
        return s[si - leng:si]
    else:
        return int(s[si - leng:si], 2)


def dec_packet():
    global s, si, versions

    my_packet = {"packets": []}
    V = gets(3)
    T = gets(3)
    my_packet['V'] = V
    my_packet['T'] = T
    versions += V

    if T == 4:
        # literal value
        vals = []
        last_type = 1
        while last_type > 0:
            last_type = gets(1)
            val: str = gets(4, "str")
            vals.append(val)

        realval = int("".join(vals), 2)
        my_packet["val"] = realval
    else:
        # operator
        I = gets(1)
        if I == 0:
            ll = 15
        elif I == 1:
            ll = 11
        else:
            assert False

        L = gets(ll)
        curr_i = si
        if I == 0:
            while si < curr_i + L:
                my_packet["packets"].append(dec_packet())
        elif I == 1:
            for i in range(L):
                my_packet["packets"].append(dec_packet())
        else:
            assert False

        my_packet["val"] = oper(T, my_packet)

    return my_packet


pack = dec_packet()


def part1():
    return versions


def part2():
    return pack["val"]


print("part1:", part1())
print("part2:", part2())
