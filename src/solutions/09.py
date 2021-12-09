from src.utils.utils import *

pp = print

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)


def is_low(arr, x, y):
    low = True
    me = arr[x][y]
    if x > 0:
        if (arr[x - 1][y]) <= me:
            low = False
    if x < len(arr) - 1:
        if (arr[x + 1][y]) <= me:
            low = False
    if y > 0:
        if (arr[x][y - 1]) <= me:
            low = False
    if y < len(arr[0]) - 1:
        if (arr[x][y + 1]) <= me:
            low = False

    return low


def part1():
    arr = []
    for line in slines:
        arr.append([int(x) for x in line])
    return sum([1 + arr[x][y] for x in range(len(arr)) for y in range(len(arr[0])) if is_low(arr, x, y)])


def part2():
    arr = []
    low_arr = []
    group_name_to_group = {}
    coords_to_group_name = {}
    for x, line in enumerate(slines):
        arr.append([int(c) for c in line])
        low_arr.append([0 for _ in line])
        for y, num in enumerate(line):
            group_name_to_group[(x, y)] = {(x, y)}
            coords_to_group_name[(x, y)] = (x, y)

    for x, line in enumerate(slines):
        for y, num in enumerate(line):
            my_coord = (x, y)
            my_value = arr[my_coord[0]][my_coord[1]]
            my_group_name = coords_to_group_name[my_coord]
            if my_group_name is None:
                continue

            if x > 0:
                his_coord: (int, int) = (x - 1, y)
                if my_value < (arr[his_coord[0]][his_coord[1]]) < 9:
                    his_group_name = coords_to_group_name[his_coord]
                    if his_group_name != my_group_name:
                        his_group = group_name_to_group[his_group_name]
                        # add his group to mine
                        group_name_to_group[my_group_name] |= his_group
                        for coord in group_name_to_group[his_group_name]:
                            # set his group members to have my group name
                            coords_to_group_name[coord] = my_group_name
                        # empty his group
                        group_name_to_group[his_group_name] = None

            if x < len(arr) - 1:
                his_coord = (x + 1, y)
                if my_value < (arr[his_coord[0]][his_coord[1]]) < 9:
                    his_group_name = coords_to_group_name[his_coord]
                    if his_group_name != my_group_name:
                        his_group = group_name_to_group[his_group_name]
                        group_name_to_group[my_group_name] |= his_group
                        for coord in group_name_to_group[his_group_name]:
                            coords_to_group_name[coord] = my_group_name
                        group_name_to_group[his_group_name] = None

            if y > 0:
                his_coord = (x, y - 1)
                if my_value < (arr[his_coord[0]][his_coord[1]]) < 9:
                    his_group_name = coords_to_group_name[his_coord]
                    if his_group_name != my_group_name:
                        his_group = group_name_to_group[his_group_name]
                        group_name_to_group[my_group_name] |= his_group
                        for coord in group_name_to_group[his_group_name]:
                            coords_to_group_name[coord] = my_group_name
                        group_name_to_group[his_group_name] = None

            if y < len(arr[0]) - 1:
                his_coord = (x, y + 1)
                if my_value < (arr[his_coord[0]][his_coord[1]]) < 9:
                    his_group_name = coords_to_group_name[his_coord]
                    if his_group_name != my_group_name:
                        his_group = group_name_to_group[his_group_name]
                        group_name_to_group[my_group_name] |= his_group
                        for coord in group_name_to_group[his_group_name]:
                            coords_to_group_name[coord] = my_group_name
                        group_name_to_group[his_group_name] = None

    sizes = []
    for k, v in group_name_to_group.items():
        if v is not None:
            sizes.append(len(v))

    sizes = sorted(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]


print("part1:", part1())
print("part2:", part2())
