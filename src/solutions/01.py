from utils.utils import *

lines = get_input(__file__)
numlines = lines_to_nums(lines)


def part1(nums):
    incr = 0
    cur = nums[0]
    for num in nums:
        if num > cur:
            incr += 1
        cur = num
    return incr


def part2():
    nums = []
    for i in range(len(numlines)):
        if i < len(numlines) - 2:
            nums.append(numlines[i] + numlines[i + 1] + numlines[i + 2])
    return part1(nums)


print("part1:", part1(numlines))
print("part2:", part2())
