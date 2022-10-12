from typing import Dict, Tuple, Optional

from src.utils.utils import *

# lines = get_input(__file__)
lines = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#  
  #########  """
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

pp(lines)


def part1():
    # done by hand
    return 16000 + 1200 + 180 + 20


print("part1:", part1())
