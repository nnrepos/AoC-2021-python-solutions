from utils.utils import *

lines = get_input(__file__)
lines_as_nums = lines_to_nums(lines)


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
    for i in range(len(lines_as_nums)):
        if i < len(lines_as_nums) - 2:
            nums.append(lines_as_nums[i] + lines_as_nums[i + 1] + lines_as_nums[i + 2])
    return part1(nums)


print("part1:", part1(lines_as_nums))
print("part2:", part2())
