from functools import reduce
from operator import itemgetter, mul

# import numpy as np

file = open("day8.txt", "r")
content = file.read()


boxes = list(map(lambda line: list(map(int, line.split(","))), content.splitlines()))
circuits = list(map(lambda x: [x], boxes))


def try_join(b1, b2):
    i1 = 0
    for i, circuit in enumerate(circuits):
        if b1 in circuit:
            i1 = i
            break
    i2 = 0
    for i, circuit in enumerate(circuits):
        if b2 in circuit:
            i2 = i
            break

    if i1 == i2:
        return

    # merge the second circuit into the first
    circuits[i1] += circuits[i2]
    circuits.pop(i2)


def dist_sq(b1, b2):
    return (
        (b1[0] - b2[0]) * (b1[0] - b2[0])
        + (b1[1] - b2[1]) * (b1[1] - b2[1])
        + (b1[2] - b2[2]) * (b1[2] - b2[2])
    )


pairs = []
for i, b1 in enumerate(boxes):
    for b2 in boxes[i + 1 :]:
        pairs.append((b1, b2, dist_sq(b1, b2)))
pairs.sort(key=itemgetter(2))  # 200ms on my machine

answer = 0
i = 0
while len(circuits) > 1:
    pair = pairs[i]
    try_join(pair[0], pair[1])
    answer = pair[0][0] * pair[1][0]
    i += 1
print(answer)
# circuits.sort(key=len, reverse=True)

# print(reduce(mul, map(lambda x: len(x), circuits[:3])))
