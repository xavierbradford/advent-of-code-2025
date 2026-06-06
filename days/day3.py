file = open("day3.txt", "r")
content = file.read()

total = 0
for line in content.splitlines():
    if line == "":
        continue
    batteries = [int(char) for char in line]
    cells = []
    while len(cells) < 12:
        x = 11 - len(cells)
        rest_of_batteries = batteries[:-x]
        if x == 0:
            rest_of_batteries = batteries
        max_cell = max(rest_of_batteries)
        max_index = batteries.index(max_cell)
        batteries = batteries[(max_index + 1) :]
        cells.append(max_cell)
    total += sum([cell * 10**i for i, cell in enumerate(reversed(cells))])

print(total)
