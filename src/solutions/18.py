from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)


# note: next time i'll just use the binarytree module...

class Snail:
    def __init__(self, unparsed, parent=None):
        self.right = self.left = self.val = None
        self.parent = parent

        lr = prs(unparsed)
        if type(lr) is tuple:
            left, right = lr
            self.left = Snail(left, self)
            self.right = Snail(right, self)
        else:
            self.val = lr

    def add(self, other):
        self.left = self.copy()
        self.right = other
        self.left.parent = self
        self.right.parent = self

    def copy(self):
        return Snail(str(self))

    def is_leaf(self):
        return self.val is not None

    def step(self):
        if self.explode():
            return True
        if self.split():
            return True
        return False

    def find_right(self):
        curr = self
        found = False
        while curr.parent is not None:
            # find branch to the right of mine
            if curr is curr.parent.left:
                found = True
                curr = curr.parent.right
                break
            else:
                curr = curr.parent

        if found:
            # find leftmost child or right branch
            while curr.left is not None:
                curr = curr.left

            return curr
        else:
            return False

    def find_left(self):
        curr = self
        found = False
        while curr.parent is not None:
            # find branch to the right of mine
            if curr is curr.parent.right:
                found = True
                curr = curr.parent.left
                break
            else:
                curr = curr.parent

        if found:
            # find leftmost child or right branch
            while curr.right is not None:
                curr = curr.right

            return curr
        else:
            return False

    def explode(self, depth=0):
        if depth == 4 and not self.is_leaf():
            assert self.left is not None
            assert self.right is not None
            assert self.left.val is not None
            assert self.right.val is not None
            my_left = self.find_left()
            my_right = self.find_right()
            if my_left:
                my_left.val += self.left.val
            if my_right:
                my_right.val += self.right.val

            self.right = None
            self.left = None
            self.val = 0

            return True

        if self.left is not None:
            if self.left.explode(depth + 1):
                return True

        if self.right is not None:
            if self.right.explode(depth + 1):
                return True

        return False

    def split(self):
        if self.val is not None and self.val > 9:
            self.left = Snail(un_prs(self.val // 2), self)
            self.right = Snail(un_prs(self.val - self.left.val), self)
            self.val = None
            return True

        if self.left is not None:
            if self.left.split():
                return True

        if self.right is not None:
            if self.right.split():
                return True

        return False

    def magnitude(self):
        if self.is_leaf():
            return self.val

        return self.left.magnitude() * 3 + self.right.magnitude() * 2

    def where(self):
        ans = ""
        curr = self
        while curr.parent is not None:
            if curr is curr.parent.left:
                ans = "->left" + ans
            else:
                ans = "->right" + ans

            curr = curr.parent

        return "root" + ans

    def __str__(self):
        return self.get_str([''])

    def get_str(self, st):
        if self.is_leaf():
            st[0] += str(self.val)
        else:
            st[0] += '['
            self.left.get_str(st)
            st[0] += ','
            self.right.get_str(st)
            st[0] += ']'

        return st[0]


def un_prs(num):
    return str(num)


def prs(unparsed: str):
    if not unparsed.startswith('['):
        return int(unparsed)

    num_par = 0
    unparsed = unparsed[1:-1]
    a, b = None, None

    for i, c in enumerate(unparsed):
        if c == '[':
            num_par += 1
        elif c == ']':
            num_par -= 1
        elif c == ',':
            if num_par == 0:
                a = unparsed[:i]
                b = unparsed[i + 1:]
                break

    return a, b


def part1():
    s = Snail(slines[0])
    for snail_str in range(1, nlines):
        s2 = Snail(slines[snail_str])
        s.add(s2)
        while s.step():
            pass
    return s.magnitude()


def part2():
    max_sum = 0
    pairs = [(i, j) for i in range(nlines) for j in range(nlines) if i != j]
    for i, j in pairs:
        s1 = Snail(slines[i])
        s2 = Snail(slines[j])
        s1.add(s2)
        while s1.step():
            pass
        max_sum = max(max_sum, s1.magnitude())

    return max_sum


print("part1:", part1())
print("part2:", part2())
