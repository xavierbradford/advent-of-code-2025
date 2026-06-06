file = open("day1.txt", "r")


def parse_line(line):
    return int(line[1:]) * (1 if line[0] == "R" else -1)


lines = [parse_line(line) for line in file.read().splitlines()]

total = 0
dial = 50
for line in lines:
    sign = 1 if line > 0 else -1
    while line != 0:
        dial += sign
        line -= sign
        if dial % 100 == 0:
            total += 1

print(total)
