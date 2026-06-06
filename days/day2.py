file = open("day2.txt", "r")


def parse_range(rng):
    return (int(rng.split("-")[0]), int(rng.split("-")[1]))


ranges = [parse_range(rng) for rng in file.read().split(",")]


def invalid_id(id):
    for i in range(2, len(id) + 1):
        if id == id[: len(id) // i] * i:
            # print(id[: len(id) // i], "*", i)
            return True
    return False


total = 0
for rng in ranges:
    for id in range(rng[0], rng[1] + 1, 1):
        if invalid_id(str(id)):
            total += id

print(total)
