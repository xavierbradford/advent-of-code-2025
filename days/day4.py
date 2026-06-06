file = open("test.txt", "r")
content = file.read()
papers = []

for line in content.splitlines():
    papers.append([])
    for char in line:
        papers[-1].append(char == "@")


def get(i, j):
    if i < 0 or j < 0:
        return False
    try:
        return papers[i][j]
    except IndexError:
        return False


def count_neighbours(i, j):
    return (
        get(i - 1, j - 1)
        + get(i - 1, j)
        + get(i - 1, j + 1)
        + get(i, j - 1)
        + get(i, j + 1)
        + get(i + 1, j - 1)
        + get(i + 1, j)
        + get(i + 1, j + 1)
    )


total = 0

removed = 999999999999

while removed:
    new_papers = papers.copy()
    removed = 0
    for i in range(len(papers)):
        for j in range(len(papers[i])):
            if get(i, j) and count_neighbours(i, j) < 4:
                removed += 1
                new_papers[i][j] = False
    papers = new_papers
    total += removed


print(total)
