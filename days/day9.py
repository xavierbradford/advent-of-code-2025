file = open("day9.txt", "r")
content = file.read()
points = [
    (int(line.split(",")[0]), int(line.split(",")[1])) for line in content.splitlines()
]

x_vals = sorted(set([point[0] for point in points]))
y_vals = sorted(set([point[1] for point in points]))

shading = [["." for _ in x_vals] for _ in y_vals]

for i in range(len(points)):
    points[i] = (x_vals.index(points[i][0]), y_vals.index(points[i][1]))

for i in range(len(points)):
    p1 = points[i - 1]
    p2 = points[i]
    shading[p1[1]][p1[0]] = "#"
    if p1[0] == p2[0]:
        top = min(p1[1], p2[1])
        bottom = max(p1[1], p2[1])
        for i in range(top + 1, bottom):
            shading[i][p1[0]] = "X"
    if p1[1] == p2[1]:
        left = min(p1[0], p2[0])
        right = max(p1[0], p2[0])
        for i in range(left + 1, right):
            shading[p1[1]][i] = "X"


def raycast(j, i, direction):
    if direction == "right":
        for k in shading[j][i:]:
            if k in "#X":
                return True
        return False
    elif direction == "left":
        for k in shading[j][:i]:
            if k in "#X":
                return True
        return False
    elif direction == "down":
        for row in shading[j:]:
            if row[i] in "#X":
                return True
        return False
    elif direction == "up":
        for row in shading[:j]:
            if row[i] in "#X":
                return True
        return False
    else:
        return True


for j, row in enumerate(shading):
    for i, cell in enumerate(row):
        if cell != ".":
            continue
        if not raycast(j, i, "up"):
            continue
        if not raycast(j, i, "down"):
            continue
        if not raycast(j, i, "left"):
            continue
        if not raycast(j, i, "right"):
            continue
        shading[j][i] = "v"

for line in shading:
    print("".join(line))


def is_completely_shaded(p1, p2):
    for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
        if shading[min(p1[1], p2[1])][i] == ".":
            return False
        if shading[max(p1[1], p2[1])][i] == ".":
            return False
    for j in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
        if shading[j][min(p1[0], p2[0])] == ".":
            return False
        if shading[j][max(p1[0], p2[0])] == ".":
            return False
    return True


max_area = 0
for i, p1 in enumerate(points):
    for p2 in points[:i]:
        # fake_area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
        real_area = (abs(x_vals[p2[0]] - x_vals[p1[0]]) + 1) * (
            abs(y_vals[p2[1]] - y_vals[p1[1]]) + 1
        )

        if is_completely_shaded(p1, p2):
            if real_area > max_area:
                # print("rectangle from", p1, "to", p2)
                max_area = max(max_area, real_area)

print(max_area)
