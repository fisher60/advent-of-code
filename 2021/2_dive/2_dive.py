from typing import Optional

with open("2_dive.txt", "r") as f:
    instructions = f.read().split("\n")


def get_cleaned_instructions(inp: list) -> list:
    """Convert instructions to tuples of (direction, value)"""
    for line in inp:
        direction, amount = line.split()
        yield direction, int(amount)


class Position:
    """Object for trackign state of the submarine."""
    def __init__(self, use_aim: bool):
        self.use_aim = use_aim
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def __str__(self):
        """Return the product of the horizontal and depth"""
        return str(self.horizontal * self.depth)

    def up(self, amount) -> None:
        if self.use_aim:
            self.aim -= amount
        else:
            self.depth -= amount

    def down(self, amount) -> None:
        if self.use_aim:
            self.aim += amount
        else:
            self.depth += amount

    def forward(self, amount) -> None:
        self.horizontal += amount
        if self.use_aim:
            self.depth += self.aim * amount


def parse_positions(inps: list, use_aim: Optional[bool] = False) -> Position:
    """Parse movement instructions for a position object"""
    this_pos = Position(use_aim)

    for direction, amount in inps:
        getattr(this_pos, direction)(amount)

    return this_pos


if __name__ == '__main__':
    cleaned_instr = list(get_cleaned_instructions(instructions))
    print(f"Part 1: {parse_positions(cleaned_instr)}")
    print(f"Part 2: {parse_positions(cleaned_instr, use_aim=True)}")
