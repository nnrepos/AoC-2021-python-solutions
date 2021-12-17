from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

target = parse("target area: x={}..{}, y={}..{}", lines)
minx, maxx, miny, maxy = (int(z) for z in target)
maxx += 1
maxy += 1


def part1():
    best_y = 0
    for startx in range(1, 205):
        for starty in range(0, 200):
            vx, vy = startx, starty
            xx, yy = 0, 0
            reached = False
            curr_best_y = 0
            while xx <= maxx and yy >= miny:
                xx += vx
                yy += vy
                curr_best_y = max(curr_best_y, yy)
                if vx > 0:
                    vx -= 1
                vy -= 1
                if xx in range(minx, maxx) and yy in range(miny, maxy):
                    reached = True
                    break
            if reached and best_y < curr_best_y:
                best_y = curr_best_y

    return best_y


def part2():
    ans = 0
    # explanation: if vx>maxx we instantly miss. if vy<miny, same thing.
    # if i remember my physics correctly, when starty>0, and the satelite returns to xx=0,
    # vy becomes -starty. so vy > max(|maxy|,|miny|) is also pointless.
    for startx in range(1, 205):
        for starty in range(-150, 200):
            vx, vy = startx, starty
            xx, yy = 0, 0
            reached = False
            curr_best_y = 0
            while xx <= maxx and yy >= miny:
                xx += vx
                yy += vy
                curr_best_y = max(curr_best_y, yy)
                if vx > 0:
                    vx -= 1
                vy -= 1
                if xx in range(minx, maxx) and yy in range(miny, maxy):
                    reached = True
                    break
            if reached:
                ans += 1

    return ans


print("part1:", part1())
print("part2:", part2())
