import requests
import json
from os import path

ADVENT = "https://adventofcode.com/2019/day/"
COOKIE = {'session': "53616c7465645f5fe8541fc55126eeb99c8e09d7e915070f86461773db04792003311e268eb243550fa1228c0ca57284"}
INPUTS_FILE = "inputs.json"


def mandist(x, y, xx, yy):
    return abs(x - xx) + abs(y - yy)


def get_input(filename):
    """get input from the advent website only if i don't have it yet"""
    # get day number from file name, using __file__
    day = (path.splitext(path.basename(filename))[0]).lstrip("0")

    with open(INPUTS_FILE) as f:
        # read json file
        inputs_dict = json.loads(f.read())

    if day in inputs_dict:
        return inputs_dict[day]

    else:
        # day not in json, get it from website and add it
        uri = ADVENT + day + "/input"
        resp = requests.get(uri, cookies=COOKIE)

        if "Please log in" in resp.text:
            # error
            print("login failed")
        else:
            # success
            inputs_dict[day] = resp.text
            with open(INPUTS_FILE, "w") as f:
                f.write(json.dumps(inputs_dict))

            return resp.text
