file = open("day5.txt", "r")
content = file.read()

[part1, part2] = content.split("\n\n")
ranges = list(map(lambda text: list(map(int, text.split("-"))), part1.splitlines()))
ranges.sort(key=lambda rng: -rng[0])

total = 0
prev = None
while ranges:
    rng = ranges.pop()
    if prev and rng[0] <= prev[1]:
        # merge the two
        print(
            "merging ranges",
            prev,
            rng,
            "into",
            [min(prev[0], rng[0]), max(prev[1], rng[1])],
        )
        prev = [min(prev[0], rng[0]), max(prev[1], rng[1])]
    elif prev:
        # these do not overlap... apply prev
        total += prev[1] - prev[0] + 1
        print("applying range", prev)
        prev = rng
    else:
        prev = rng
if prev:
    print("applying range", prev)
    total += prev[1] - prev[0] + 1

print("fresh foods:", total)
