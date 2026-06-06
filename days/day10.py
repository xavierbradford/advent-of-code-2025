file = open("day10.txt", "r")


def parse_line(line):
    split = line.split(" ")
    return (
        [x == "#" for x in split[0][1:-1]],
        [[int(x) for x in schematic[1:-1].split(",")] for schematic in split[1:-1]],
        [int(x) for x in split[-1][1:-1].split(",")],
    )


lines = [parse_line(line) for line in file.read().splitlines()]

# total = 0
# for line in lines:
#     min_presses = 99999999
#     for combination in range(2 ** len(line[1])):
#         # try this combination of thingzzz
#         light_state = [False for _ in line[0]]
#         button_presses = 0
#         for button in range(len(line[1])):
#             if combination >> button & 1:
#                 # apply this button
#                 button_presses += 1
#                 for effect in line[1][button]:
#                     light_state[effect] = not light_state[effect]
#         if light_state == line[0]:
#             # print(
#             #     ("{:0" + str(len(line[1])) + "b}: {}").format(
#             #         combination, button_presses
#             #     )
#             # )
#             min_presses = min(min_presses, button_presses)
#     total += min_presses

# print(total)


def multi_for(iterables):
    if not iterables:
        yield ()
    else:
        for item in iterables[0]:
            for rest_tuple in multi_for(iterables[1:]):
                yield (item,) + rest_tuple


asdfasdfasd = 0
for line in lines:
    button_count = len(line[1])
    joltage_count = len(line[2])
    matrix = [[] for _ in range(joltage_count)]
    # add the button effects
    for button in line[1]:
        for i in range(joltage_count):
            matrix[i].append(1 if i in button else 0)

    # augment the matrix
    for i, val in enumerate(line[2]):
        matrix[i].append(val)

    print("Start:")
    for row in matrix:
        # print(" ".join(row))
        print(" ".join(map(str, row)))

    def subtract_row_from_row(row_1, row_2, multiplier=1):
        for i, val in enumerate(matrix[row_1]):
            matrix[row_2][i] -= val * multiplier

    def swap_rows(row_1, row_2):
        matrix[row_1], matrix[row_2] = matrix[row_2], matrix[row_1]

    # [0, 0, 4, 0, 0, 0, 4, -2, 2, 0, 2, 4, 2, 290]

    def normalize_row(row):
        leading_value = 0
        for i, val in enumerate(matrix[row]):
            if leading_value == 0 and val != 0:
                leading_value = val
            if leading_value != 0:
                matrix[row][i] /= leading_value

    # actually do the thing
    head_row = 0
    for button_index in range(button_count):
        # find the pivot in that column
        pivot_row = None
        for row in range(joltage_count):
            if (
                matrix[row][:button_index] == [0] * button_index
                and matrix[row][button_index] != 0
            ):
                pivot_row = row
                normalize_row(pivot_row)
                # print("normalized:", matrix[pivot_row])
                swap_rows(head_row, pivot_row)
                break
        if pivot_row is None:
            continue  # undefined behaviour
        print("Pivot for col", button_index, "was found in row", pivot_row)
        print("Intermediate Result (after pivot alignment):")
        for row in matrix:
            print(" ".join(map(str, row)))
        for row in range(joltage_count):
            if row == head_row:
                continue  # skip subtracting the row from itself lmfao
            subtract_row_from_row(head_row, row, matrix[row][button_index])
        print("Intermediate Result (after subtracting):")
        for row in matrix:
            print(" ".join(map(str, row)))
        head_row += 1
    print("Result:")

    for row in matrix:
        print(" ".join(map(str, map(int, row))))
    free_vars = []
    for i in range(button_count):
        count = 0
        for j in range(joltage_count):
            if matrix[j][i] != 0:
                count += 1
        if count == 0:
            print("button", i, "is unbound 🚨")
        elif count == 1:
            print("button", i, "is fixed")
        else:
            free_vars.append(i)
            print("button", i, "is free ⚠️")

    presses_upper_bound = max(line[2])
    print(free_vars)

    min_presses = 99999999
    sol_acc = None
    for i in multi_for([range(presses_upper_bound + 1) for _ in free_vars]):
        total_presses = 0
        acc = [0 for _ in line[2]]
        for r, row in enumerate(matrix):
            if all(map(lambda x: abs(x) < 0.1, row)):
                continue
            float_presses = row[-1] + sum(
                [-row[var] * i[ind] for ind, var in enumerate(free_vars)]
            )
            presses = round(float_presses)
            if presses < 0 or abs(presses - float_presses) > 0.1:
                # invalid attempt.
                presses = 9999999999
            # print(
            #     "pressing button",
            #     row.index(1),
            #     ",",
            #     presses,
            #     "times",
            # )
            for effect in line[1][row.index(1)]:
                acc[effect] += presses
            total_presses += presses
        for ind, free_var in enumerate(free_vars):
            # print("pressing button", free_var, ",", i[ind], "times")
            total_presses += i[ind]
            for effect in line[1][free_var]:
                acc[effect] += i[ind]

        if total_presses < min_presses:
            min_presses = total_presses
            sol_acc = acc
    if sol_acc != line[2]:
        print(sol_acc, line[2])
        raise Exception("fuck")
    print(
        min_presses,
    )
    asdfasdfasd += min_presses

print("answer", asdfasdfasd)
