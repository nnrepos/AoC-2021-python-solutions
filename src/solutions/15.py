from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

gr = defaultdict(lambda: dict())
dist = defaultdict(lambda: float("inf"))
unvisited = []
cols = 0
rows = len(slines)


def rowcol_to_node(row, col):
    return row * cols + col


def node_to_rowcol(node_id):
    return node_id // cols, node_id % cols


def get_nei(node_id):
    my_row, my_col = node_to_rowcol(node_id)
    nei = []
    if my_row + 1 in range(rows):
        nei.append(rowcol_to_node(my_row + 1, my_col))
    if my_row - 1 in range(rows):
        nei.append(rowcol_to_node(my_row - 1, my_col))
    if my_col + 1 in range(cols):
        nei.append(rowcol_to_node(my_row, my_col + 1))
    if my_col - 1 in range(cols):
        nei.append(rowcol_to_node(my_row, my_col - 1))

    return nei


def dijkstra(start):
    global unvisited
    curr = start
    while curr is not None:
        for nei in get_nei(curr):
            if nei in unvisited:
                dist[nei] = min(dist[nei], dist[curr] + gr[curr][nei])

        if unvisited:
            curr = unvisited[0]
            for node in unvisited:
                if dist[node] < dist[curr]:
                    curr = node

            if dist[curr] == float("inf"):
                print("dijkstra inf")
                return
            if node_to_rowcol(curr) == (rows - 1, cols - 1):
                print("dijkstra dest")
                return
            unvisited.remove(curr)
        else:
            print("dijkstra all")
            curr = None


def part1():
    global rows, cols, unvisited, gr, dist
    for row, ll in enumerate(slines):
        cols = len(ll)
        for col, w in enumerate(ll):
            weight = int(w)
            node_id = row * len(ll) + col
            unvisited.append(node_id)
            if col - 1 in range(cols):
                gr[rowcol_to_node(row, col - 1)][node_id] = weight
            if col + 1 in range(cols):
                gr[rowcol_to_node(row, col + 1)][node_id] = weight
            if row - 1 in range(rows):
                gr[rowcol_to_node(row - 1, col)][node_id] = weight
            if row + 1 in range(rows):
                gr[rowcol_to_node(row + 1, col)][node_id] = weight

    dist[rowcol_to_node(0, 0)] = 0

    dijkstra(rowcol_to_node(0, 0))

    return dist[rowcol_to_node(rows - 1, cols - 1)]


def part2():
    return


print("part1:", part1())
print("part2:", part2())
