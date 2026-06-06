file = open("day11.txt", "r")

graph = {}
for line in file.read().splitlines():
    [parent, children] = line.split(":")
    children = children.split(" ")[1:]
    graph[parent] = children

paths = {}


def count_paths(start, end, dac, fft):
    if start == end:
        paths[(start, end, dac, fft)] = int(dac and fft)
        return int(dac and fft)
    elif (start, end, dac, fft) in paths:
        return paths[(start, end, dac, fft)]
    else:
        result = sum(
            map(
                lambda child: count_paths(
                    child, end, dac or (child == "dac"), fft or (child == "fft")
                ),
                graph[start],
            )
        )
        paths[(start, end, dac, fft)] = result
        return result


print(count_paths("svr", "out", False, False))
