from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)


def add_mod_ten(arr, i, j):
    arr[i][j] = (arr[i][j] + 1) % 10


def add_max_zero_val(arr, i, j, val):
    arr[i][j] = (arr[i][j] + val)
    if arr[i][j] > 9:
        arr[i][j] = 0


def inc_arr(arr):
    for i, row in enumerate(arr):
        for j, col in enumerate(arr):
            arr[i][j] = (arr[i][j] + 1) % 10


def add_mod_nei(add_arr, i, j):
    blen = len(add_arr)
    slen = len(add_arr[0])
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == dj == 0:
                continue
            if (i + di) in range(blen) and (j + dj) in range(slen):
                add_mod_ten(add_arr, i + di, j + dj)


def check_flash_once(arr, flashed, add_arr, flsh):
    flash_done = True
    for i, row in enumerate(arr):
        for j, col in enumerate(arr):
            if arr[i][j] == 0 and not flashed[i][j]:
                flashed[i][j] = True
                flsh += 1
                flash_done = False
                add_mod_nei(add_arr, i, j)
    return flash_done, flsh


def merge_arrs(arr, add_arr):
    for i, row in enumerate(arr):
        for j, col in enumerate(arr):
            add_max_zero_val(arr, i, j, add_arr[i][j])


def reset_flashed(arr, flashed):
    sync = True
    for i, row in enumerate(arr):
        for j, col in enumerate(arr):
            if flashed[i][j]:
                arr[i][j] = 0
            else:
                sync = False
    return sync


def part1_pretty():
    arr = [[int(x) for x in s] for s in slines]
    flsh = 0
    for step in range(100):
        inc_arr(arr)
        flashed = [[False for _ in s] for s in slines]
        flash_done = False
        while not flash_done:
            add_arr = [[0] * len(arr[0]) for _ in range(len(arr))]
            flash_done, flsh = check_flash_once(arr, flashed, add_arr, flsh)
            merge_arrs(arr, add_arr)
        reset_flashed(arr, flashed)

    return flsh


def part2_pretty():
    arr = [[int(x) for x in s] for s in slines]
    flsh = 0
    sync = False
    steps = 0
    while not sync:
        steps += 1
        inc_arr(arr)
        flashed = [[False for _ in s] for s in slines]
        flash_done = False
        while not flash_done:
            add_arr = [[0] * len(arr[0]) for _ in range(len(arr))]
            flash_done, flsh = check_flash_once(arr, flashed, add_arr, flsh)
            merge_arrs(arr, add_arr)
        sync = reset_flashed(arr, flashed)

    return steps


def part1():
    arr = [[int(x) for x in s] for s in slines]
    flsh = 0
    for step in range(100):
        for i, row in enumerate(arr):
            for j, col in enumerate(arr):
                arr[i][j] = (arr[i][j] + 1) % 10
        flashed = [[False for _ in s] for s in slines]
        flash_done = False
        while not flash_done:
            flash_done = True
            add_arr = [[0] * len(arr[0]) for _ in range(len(arr))]
            for i, row in enumerate(arr):
                for j, col in enumerate(arr):
                    if arr[i][j] == 0 and not flashed[i][j]:
                        flashed[i][j] = True
                        flsh += 1
                        flash_done = False
                        blen = len(arr)
                        slen = len(arr[0])
                        for di in range(-1, 2):
                            for dj in range(-1, 2):
                                if di == dj == 0:
                                    continue
                                if (i + di) in range(blen) and (j + dj) in range(slen):
                                    add_mod_ten(add_arr, i + di, j + dj)

            for i, row in enumerate(arr):
                for j, col in enumerate(arr):
                    add_max_zero_val(arr, i, j, add_arr[i][j])

        for i, row in enumerate(arr):
            for j, col in enumerate(arr):
                if flashed[i][j]:
                    arr[i][j] = 0

    return flsh


def part2():
    arr = [[int(x) for x in s] for s in slines]
    flsh = 0
    sync = False
    steps = 0
    while not sync:
        sync = True
        steps += 1
        for i, row in enumerate(arr):
            for j, col in enumerate(arr):
                arr[i][j] = (arr[i][j] + 1) % 10
        flashed = [[False for _ in s] for s in slines]
        flash_done = False
        while not flash_done:
            flash_done = True
            add_arr = [[0] * len(arr[0]) for _ in range(len(arr))]
            for i, row in enumerate(arr):
                for j, col in enumerate(arr):
                    if arr[i][j] == 0 and not flashed[i][j]:
                        flashed[i][j] = True
                        flsh += 1
                        flash_done = False
                        blen = len(arr)
                        slen = len(arr[0])
                        for di in range(-1, 2):
                            for dj in range(-1, 2):
                                if di == dj == 0:
                                    continue
                                if (i + di) in range(blen) and (j + dj) in range(slen):
                                    add_mod_ten(add_arr, i + di, j + dj)

            for i, row in enumerate(arr):
                for j, col in enumerate(arr):
                    add_max_zero_val(arr, i, j, add_arr[i][j])

        for i, row in enumerate(arr):
            for j, col in enumerate(arr):
                if flashed[i][j]:
                    arr[i][j] = 0
                else:
                    sync = False

    return steps


print("part1:", part1_pretty())
print("part2:", part2_pretty())
