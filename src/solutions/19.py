from src.utils.utils import *
from itertools import permutations

# lines = get_input(__file__)
lines="""--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""
slines = lines.splitlines()
nlines = len(slines)
lines_as_nums = lines_to_nums(lines)

pp(lines)

PERMS = [(sign_x, sign_y, sign_z, order) for sign_x in (-1, 1) for sign_y in (-1, 1) for sign_z in (-1, 1) for order in permutations((0, 1, 2))]

scanners = []
curr_scanner = []
for ll in slines[1:]:
    if "scanner" in ll:
        scanners.append(curr_scanner)
        curr_scanner = []
    elif "," in ll:
        curr_scanner.append([int(x) for x in ll.strip().split(",")])


def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


def is_similar(his_scanner, my_dist_sizes):
    # for all permutations:
    #     similar distances = compare distances of all pairs
    #     if similar distances >= 12:
    #         save permutation, add scanner to list
    his_distances = [(x - xx, y - yy, z - zz) for i, (x, y, z) in enumerate(his_scanner) for j, (xx, yy, zz) in enumerate(his_scanner) if i != j]
    his_dist_sizes = defaultdict(lambda: [])
    for x, y, z in his_distances:
        his_dist_sizes[norm(x, y, z)].append((x, y, z))

    for perm in PERMS:
        equal_distances = 0
        (sign_x, sign_y, sign_z, order) = perm
        x_i, y_i, z_i = order
        for k, v in my_dist_sizes.items():
            if k in his_dist_sizes:
                # distances can only be equal if they have the same size
                for his_dist in his_dist_sizes[k]:
                    for my_dist in my_dist_sizes[k]:
                        xx, yy, zz = my_dist
                        x, y, z = his_dist[x_i] * sign_x, his_dist[y_i] * sign_y, his_dist[z_i] * sign_z
                        if x == xx and y == yy and z == zz:
                            equal_distances += 1
                            if equal_distances >= 12:
                                return perm
    return None


def part1():
    found_scanners = {0: ((1, 1, 1, (0, 1, 2)), 0)}
    unvisited_scanners = [0]
    while unvisited_scanners:
        my_index = unvisited_scanners.pop()
        my_scanner = scanners[my_index]
        my_distances = [(x - xx, y - yy, z - zz) for i, (x, y, z) in enumerate(my_scanner) for j, (xx, yy, zz) in enumerate(my_scanner) if i != j]
        my_dist_sizes = defaultdict(lambda: [])
        for x, y, z in my_distances:
            my_dist_sizes[norm(x, y, z)].append((x, y, z))

        for i, his_scanner in enumerate(scanners):
            if i in found_scanners:
                continue
            perm = is_similar(his_scanner, my_dist_sizes)
            if perm:
                print("found:", i, perm)
                unvisited_scanners.append(i)
                found_scanners[i] = (perm, my_index)

    # TODO: save first equal beacon, print it
    # should be equal:
    # sx, sy, sz, order = found_scanners[1][0]
    #
    # print(scanners[])
    return


def part2():
    return


print("part1:", part1())
print("part2:", part2())
