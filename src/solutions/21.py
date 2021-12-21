from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

MAX_SCORE = 1000

last_roll = 0
die_rolls = 0


def roll_die():
    global last_roll, die_rolls
    die_rolls += 1
    last_roll = last_roll % 100 + 1
    return last_roll


def next_loc(last, roll):
    return (last + roll - 1) % 10 + 1


def part1():
    score = [0, 0]
    loc = [0, 0]
    loc[0] = int(slines[0].split()[-1])
    loc[1] = int(slines[1].split()[-1])
    ended = False
    winner = 0
    while not ended:
        for i in range(2):
            for _ in range(3):
                loc[i] = next_loc(loc[i], roll_die())
            score[i] += loc[i]
            if score[i] >= MAX_SCORE:
                ended = True
                winner = i
                break

    return score[1 - winner] * die_rolls


def part2():
    loc1 = int(slines[0].split()[-1])
    loc2 = int(slines[1].split()[-1])

    state_pairs = d()  # score1, score2, loc1, loc2, curr_roll, turn
    state_pairs[(0, 0, loc1, loc2, 0, 1)] += 1
    wins1 = wins2 = 0

    while state_pairs:
        new_states = d()
        for k, v in state_pairs.items():
            score1, score2, loc1, loc2, curr_roll, turn = k
            if turn == 1:  # 1-indexed
                new_loc2 = loc2
                new_score2 = score2
                for i in range(1, 4):
                    new_curr_roll = curr_roll + 1
                    new_score1 = score1
                    new_loc1 = next_loc(loc1, i)
                    new_turn = 1

                    if new_curr_roll == 3:  # 0-indexed
                        new_turn = 2
                        new_curr_roll = 0
                        new_score1 += new_loc1

                    if new_score1 >= 21:
                        wins1 += v
                    else:
                        new_states[(new_score1, new_score2, new_loc1, new_loc2, new_curr_roll, new_turn)] += v

            else:
                new_loc1 = loc1
                new_score1 = score1
                for i in range(1, 4):
                    new_curr_roll = curr_roll + 1
                    new_score2 = score2
                    new_loc2 = next_loc(loc2, i)
                    new_turn = 2

                    if new_curr_roll == 3:  # 0-indexed
                        new_turn = 1
                        new_curr_roll = 0
                        new_score2 += new_loc2

                    if new_score2 >= 21:
                        wins2 += v
                    else:
                        new_states[(new_score1, new_score2, new_loc1, new_loc2, new_curr_roll, new_turn)] += v

        state_pairs = new_states

    return max(wins1, wins2)


print("part1:", part1())
print("part2:", part2())
