from dataclasses import dataclass

file = open("test.txt", "r")
sections = file.read().split("\n\n")


@dataclass
class Region:
    w: int
    h: int
    block_counts: list[int]


@dataclass(frozen=True, eq=True)
class Block:
    top_left: bool
    top_center: bool
    top_right: bool
    center_left: bool
    center_center: bool
    center_right: bool
    bottom_left: bool
    bottom_center: bool
    bottom_right: bool

    def rotate_cw(self):
        return Block(
            self.bottom_left,
            self.center_left,
            self.top_left,
            self.bottom_center,
            self.center_center,
            self.top_center,
            self.bottom_right,
            self.center_right,
            self.top_right,
        )

    def flip(self):
        return Block(
            self.top_right,
            self.top_center,
            self.top_left,
            self.center_right,
            self.center_center,
            self.center_left,
            self.bottom_right,
            self.bottom_center,
            self.bottom_left,
        )

    def area(self):
        return (
            self.top_left
            + self.top_center
            + self.top_right
            + self.center_left
            + self.center_center
            + self.center_right
            + self.bottom_left
            + self.bottom_center
            + self.bottom_right
        )

    def __str__(self):
        def s(b):
            return "#" if b else "."

        return (
            s(self.top_left)
            + s(self.top_center)
            + s(self.top_right)
            + "\n"
            + s(self.center_left)
            + s(self.center_center)
            + s(self.center_right)
            + "\n"
            + s(self.bottom_left)
            + s(self.bottom_center)
            + s(self.bottom_right)
        )


@dataclass
class Arrangement:
    block_counts: list[int]
    filled: list[list[bool]]


regions = list(
    map(
        lambda line: region(
            int(line.split("x")[0]),
            int(line.split("x")[1].split(" ")[0][:-1]),
            list(map(int, line.split("x")[1].split(" ")[1:])),
        ),
        sections[-1].splitlines(),
    )
)

temp = [section.split(":")[1].split("\n")[1:] for section in sections[:-1]]
blocks = [
    Block(
        b[0][0] == "#",
        b[0][1] == "#",
        b[0][2] == "#",
        b[1][0] == "#",
        b[1][1] == "#",
        b[1][2] == "#",
        b[2][0] == "#",
        b[2][1] == "#",
        b[2][2] == "#",
    )
    for b in temp
]

symmetries = [
    list(
        set(
            [
                b,
                b.rotate_cw(),
                b.rotate_cw().rotate_cw(),
                b.rotate_cw().rotate_cw().rotate_cw(),
                b.flip(),
                b.flip().rotate_cw(),
                b.flip().rotate_cw().rotate_cw(),
                b.flip().rotate_cw().rotate_cw().rotate_cw(),
            ]
        )
    )
    for b in blocks
]

for i in range(len(blocks)):
    print("-------------")
    for symmetry in symmetries[i]:
        print(symmetry)
        print()

for r in regions:
    print(r)


def try_place(board: list[list[bool]], block: Block, x: int, y: int) -> bool:
    for symmetry in

def solvable(block_count: list[int], board: list[list[bool]]) -> bool:
    necessary_area = sum(
        [blocks[i].area() * block_count[i] for i in range(len(blocks))]
    )
    width = len(board[0])
    height = len(board)
    available_area = width * height
    if available_area < necessary_area:
        return False

    # try placing the first piece anywhere
    first_piece = None
    first_piece_count = None
    for i, count in enumerate(block_count):
        if count != 0:
            first_piece = i
            first_piece_count = count
            break
    if first_piece is None:
        return True

    for x in range(width - 2):
        for y in range(height - 2):
            for symmetry in symmetries[first_piece]:
                placed = try_place(board, symmetry, x, y)
                if placed:


# for r in regions:
#     print(solvable(r.block_counts, [[False for _ in range(r.w)] for _ in range(r.h)]))
