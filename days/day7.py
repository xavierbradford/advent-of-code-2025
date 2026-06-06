import time
from random import choice

from colorama import Back, Fore, Style


def get_value(line, i):
    if line[i] == "S":
        return 1
    elif isinstance(line[i], int):
        return line[i]
    else:
        return 0


def add_value(line, i, val):
    try:
        # print(get_value(line, i) + val)
        line[i] = get_value(line, i) + val
    except IndexError:
        pass


while True:
    file = open("test.txt", "r")
    content = file.read()
    lines = list(map(list, content.splitlines()))

    prev = list(map(lambda x: ".", lines[0]))  # zero line
    for line in lines:
        for i in range(len(line)):
            previous_val = get_value(prev, i)
            if previous_val == 0:
                continue

            if line[i] == "^":
                add_value(line, i - 1, previous_val)
                add_value(line, i + 1, previous_val)
            else:
                add_value(line, i, previous_val)
        for word in line:
            style = ""
            if word == ".":
                style = Fore.BLUE + Style.DIM
            elif word == "^":
                style = (
                    choice([Fore.WHITE, Fore.RED, Fore.YELLOW, Fore.BLUE])
                    + Style.BRIGHT
                )
            else:
                style = Fore.GREEN + Style.NORMAL
            print(style + str(word).ljust(2), end="")
        print()
        prev = line

    print(
        Fore.RED
        + Style.DIM
        + str(sum(filter(lambda x: isinstance(x, int), lines[-1]), 0)).rjust(16)
    )
    time.sleep(0.1)
