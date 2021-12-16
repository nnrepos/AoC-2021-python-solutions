from src.utils.utils import *

lines = get_input(__file__)
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

gr = defaultdict(lambda: dict())
dist = defaultdict(lambda: float("inf"))
unvisited = []
cols = 0
rows = 0


def rowcol_to_node(row, col):
    return row * cols + col


def node_to_rowcol(node_id):
    return node_id // cols, node_id % cols


def get_nei(node_id):
    my_row, my_col = node_to_rowcol(node_id)
    nei = []
    for drow, dcol in ADJ:
        new_row, new_col = my_row + drow, my_col + dcol
        if new_row in range(rows) and new_col in range(cols):
            nei.append(rowcol_to_node(new_row, new_col))

    return nei


def dijkstra(start):
    global unvisited
    curr = start
    while curr is not None:
        my_dist = dist[curr]

        for nei in get_nei(curr):
            new_dist = my_dist + gr[curr][nei]
            old_dist = dist[nei]
            if new_dist < old_dist:
                dist[nei] = new_dist
                heappush(unvisited, (new_dist, nei))

        if unvisited:
            curr_dist, curr = heappop(unvisited)

            if curr_dist == float("inf"):
                print("dijkstra inf")
                return

            if node_to_rowcol(curr) == (rows - 1, cols - 1):
                # print("dijkstra dest")
                return
        else:
            print("dijkstra all")
            curr = None


def part1():
    global rows, cols, unvisited, gr, dist

    gr = defaultdict(lambda: dict())
    dist = defaultdict(lambda: float("inf"))
    unvisited = []
    heapify(unvisited)
    rows = len(slines)

    for row, ll in enumerate(slines):
        cols = len(ll)
        for col, w in enumerate(ll):
            weight = int(w)
            node_id = row * len(ll) + col
            unvisited.append((dist[node_id], node_id))

            for drow, dcol in ADJ:
                new_row, new_col = row + drow, col + dcol
                if new_row in range(rows) and new_col in range(cols):
                    gr[rowcol_to_node(new_row, new_col)][node_id] = weight

    dist[rowcol_to_node(0, 0)] = 0

    dijkstra(rowcol_to_node(0, 0))

    return dist[rowcol_to_node(rows - 1, cols - 1)]


def part2():
    global rows, cols, unvisited, gr, dist

    gr = defaultdict(lambda: dict())
    dist = defaultdict(lambda: float("inf"))
    unvisited = []
    heapify(unvisited)
    rows = len(slines)

    newslines = d()
    for row, ll in enumerate(slines):
        cols = len(ll)
        for col, w in enumerate(ll):
            w = int(w)
            for mrow in range(5):
                for mcol in range(5):
                    newslines[(row + mrow * cols, col + mcol * rows)] = str(((w + mrow + mcol - 1) % 9) + 1)

    rows *= 5
    cols *= 5
    newlines = []
    for row in range(rows):
        newline = []
        for col in range(cols):
            newline.append(newslines[(row, col)])
        newlines.append("".join(newline))

    for row, ll in enumerate(newlines):
        cols = len(ll)
        for col, w in enumerate(ll):
            weight = int(w)
            node_id = row * len(ll) + col
            unvisited.append((dist[node_id], node_id))

            for drow, dcol in ADJ:
                new_row, new_col = row + drow, col + dcol
                if new_row in range(rows) and new_col in range(cols):
                    gr[rowcol_to_node(new_row, new_col)][node_id] = weight

    dist[rowcol_to_node(0, 0)] = 0

    dijkstra(rowcol_to_node(0, 0))

    return dist[rowcol_to_node(rows - 1, cols - 1)]


print("part1:", part1())
print("part2:", part2())
