import json
from collections import defaultdict, Counter, deque
from functools import reduce
from heapq import heapify, heappush, heappop
from pathlib import Path
from math import sqrt

import requests
from parse import parse

from src.utils.cookie import COOKIE

# prevent optimizations
_ = (Counter, deque, reduce, heapify, heappush, heappop, parse)

# useful shortcut
pp = print

YEAR = 2021
ADVENT = f"https://adventofcode.com/{YEAR}/day/"

INPUTS_FILE = "inputs.json"
HTML_OK = 200
HTML_NOT_FOUND = 404
ADJ = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIAG = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
AROUND = ADJ + DIAG


def mandist(x, y, xx, yy):
    return abs(x - xx) + abs(y - yy)


def mandist3d(x, y, z, xx, yy, zz):
    return abs(x - xx) + abs(y - yy) + abs(z - zz)


def dist3d(x, y, z, xx, yy, zz):
    return sqrt((x - xx) ** 2 + (y - yy) ** 2 + (z - zz) ** 2)


def get_input(filename: str):
    """get input from the advent website only if i don't have it yet"""
    # get day number from file name, using __file__
    day = str(Path(filename).stem).lstrip("0")
    json_file = Path(__file__).parent / INPUTS_FILE

    if json_file.exists():
        with open(json_file) as f:
            # read json file
            inputs_dict = json.loads(f.read())

        if day in inputs_dict:
            return inputs_dict[day]

        else:
            # day not in json, get it from website and add it
            uri = f"{ADVENT}{day}/input"
            resp = requests.get(uri, cookies=COOKIE)
            if resp.status_code == HTML_OK:
                # success
                print("downloaded input")
                inputs_dict[day] = resp.text
                with open(json_file, "w") as f:
                    f.write(json.dumps(inputs_dict))
                return resp.text
            elif resp.status_code == 404:
                raise ConnectionError("page not found")
            else:
                raise ConnectionError("unknown error")
    else:
        print("creating new input json file")
        with open(json_file, "w") as f:
            f.write(json.dumps(dict()))
        return get_input(filename)


def lines_to_nums(lines):
    try:
        return [int(x) for x in lines.splitlines()]
    except ValueError:
        return None


def d():
    return defaultdict(int)
