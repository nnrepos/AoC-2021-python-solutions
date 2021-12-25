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

LETTERS = ('A', 'B', 'C', 'D')

HALLWAY = 1
DEST_ROWS = range(2, 4)

mat = []
for line in slines:
    mat.append([x for x in line])


def get_dest_col(letter: str):
    return (ord(letter) - ord('A') + 1) * 2 + 1


def is_dest_ready(letter, indexes):
    col = get_dest_col(letter)

    # check letters in dest are ok
    for row in DEST_ROWS:
        if indexes[(row, col)][0] not in (letter, '.'):
            return False

    # check letters are organized
    for i in DEST_ROWS:  # .... A... AA.. AAA.
        legal = True
        for j in DEST_ROWS:
            if j < i:
                if mat[j][col] != letter:
                    legal = False
                    break
            else:
                if mat[j][col] == letter:
                    legal = False
                    break
        if legal:
            return i

    return False


def get_energy(letter):
    return 10 ** (ord(letter) - ord('A'))


def part1():
    # done by hand
    return 16000 + 1200 + 180 + 20


def is_legal(i, j, indexes):
    if i < len(mat) and j < len(mat[0]):
        if indexes[(i, j)][0] == '.':
            return True
    return False


def is_complete(indexes):
    for letter in LETTERS:
        for row in DEST_ROWS:
            col = get_dest_col(letter)
            if indexes[(row, col)][0] != letter:
                return False
    return True


def is_hallway_clear(my_col, dest_col, indexes):
    if my_col < dest_col:
        start, end = my_col + 1, dest_col + 1
    else:
        start, end = dest_col, my_col

    return all(indexes[(1, col)][0] == '.' for col in range(start, end))


def draw_board(indexes):
    print()
    for row in range(len(DEST_ROWS) + 3):
        for col in range(len(LETTERS) * 2 + 5):
            print(indexes[(row, col)][0], end='')
        print()

# TODOniv: understand why this is inefficient.
def part1_code():
    first_indexes = dict()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            char = mat[i][j]
            assert len(char) == 1
            is_done = True
            if char in LETTERS:
                is_done = False
                if j == get_dest_col(char):
                    for k in reversed(sorted(DEST_ROWS)):
                        if k == i:  # AABB
                            is_done = True
                            break
                        if mat[k][j] != char:  # AABA
                            break

            first_indexes[(i, j)] = (char, False, is_done)

    states: Dict[Tuple[frozenset, Optional[Tuple]], int] = dict()
    states[(frozenset(first_indexes.items()), None)] = 0  # indexes, moving = energy
    best_energy = 234234234
    while states:
        new_states = dict()
        for (indexes, moving), energy in states.items():
            indexes = dict(indexes)
            assert (isinstance(indexes, dict))
            if moving is not None:
                assert (isinstance(moving, tuple))
                # some letter is already moving
                letter, (i, j), direction = moving
                new_indexes = indexes.copy()
                if direction == "right":
                    if is_legal(i, j + 1, indexes):
                        new_indexes[(i, j)] = ('.', False, True)
                        new_indexes[(i, j + 1)] = (letter, True, False)
                        new_moving = (letter, (i, j + 1), "right")
                        new_energy = energy + get_energy(letter)
                    else:
                        new_moving = None
                        new_energy = energy

                else:
                    if is_legal(i, j - 1, indexes):
                        new_indexes[(i, j)] = ('.', False, True)
                        new_indexes[(i, j - 1)] = (letter, True, False)
                        new_moving = (letter, (i, j - 1), "left")
                        new_energy = energy + get_energy(letter)
                    else:
                        new_moving = None
                        new_energy = energy

                new_state = (frozenset(new_indexes.items()), new_moving)
                if new_state in states:
                    new_energy = min(new_energy, states[new_state])
                if new_state in new_states:
                    new_energy = min(new_energy, new_states[new_state])

                new_states[new_state] = new_energy

            for (i, j), (letter, is_out, is_done) in indexes.items():
                if is_done:
                    continue

                if is_out:
                    # letter is in hallway
                    dest_col = get_dest_col(letter)
                    dest_row = is_dest_ready(letter, indexes)
                    if dest_row and is_hallway_clear(j, dest_col, indexes):
                        new_indexes: dict = indexes.copy()
                        new_indexes[(i, j)] = ('.', False, True)
                        new_indexes[(dest_row, dest_col)] = (letter, True, True)
                        new_energy = energy + (get_energy(letter) * (dest_row - 1 + abs(j - dest_col)))
                        new_moving = None

                        if is_complete(new_indexes):
                            best_energy = min(best_energy, new_energy)
                        else:
                            new_state = (frozenset(new_indexes.items()), new_moving)
                            if new_state in states:
                                new_energy = min(new_energy, states[new_state])
                            if new_state in new_states:
                                new_energy = min(new_energy, new_states[new_state])

                            new_states[new_state] = new_energy

                else:
                    # letter is in some dest and might go out
                    legal_move = True
                    for k in range(1, i):
                        if not is_legal(k, j, indexes):
                            legal_move = False

                    if legal_move:
                        for direction in ("right", "left"):
                            if direction == "right":
                                new_col = j + 1
                            else:
                                new_col = j - 1

                            if is_legal(1, new_col, indexes):
                                new_indexes: dict = indexes.copy()
                                new_indexes[(i, j)] = ('.', False, True)
                                new_indexes[(1, new_col)] = (letter, True, False)
                                new_moving = (letter, (1, new_col), direction)
                                new_energy = energy + (get_energy(letter) * i)  # i - 1 + 1

                                new_state = (frozenset(new_indexes.items()), new_moving)
                                if new_state in states:
                                    new_energy = min(new_energy, states[new_state])
                                if new_state in new_states:
                                    new_energy = min(new_energy, new_states[new_state])

                                new_states[new_state] = new_energy

        states = new_states
        print(len(states))
    return best_energy


def part2():
    return


print("part1:", part1_code())
print("part2:", part2())
