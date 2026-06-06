from functools import reduce
from operator import mul

file = open("day6.txt", "r")
content = file.read()
lines = list(map(list, content.splitlines()))


def try_get(arr, n):
    try:
        return arr[n]
    except IndexError:
        return " "


total = 0
operation = ""
nums = []
max_len = max(map(len, lines))
for i in range(max_len + 1):
    if try_get(lines[-1], i) != " ":
        operation = lines[-1][i]
    num = "".join(
        filter(lambda num: num != " ", map(lambda line: try_get(line, i), lines[:-1]))
    )
    if num != "":
        nums.append(int(num))
    else:
        if operation == "+":
            total += sum(nums)
        else:
            total += reduce(mul, nums)
        nums = []

print(total)
