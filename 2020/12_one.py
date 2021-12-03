with open("12_.txt", "r") as f:
    inputs = f.read().split("\n")

# with open("12_test.txt", "r") as f:
#     inputs = f.read().split("\n")


def split_instr(instruction):
    return instruction[0], int(instruction[1:])


class Position:
    def __init__(self, x, y, direction=90):
        self.x = x
        self.y = y
        self.direction = direction
        self.dirs = {0: "N", 90: "E", 180: "S", 270: "W"}

    def __str__(self):
        return str((self.x, self.y))

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y, self.direction)

    @property
    def cardinal_dir(self):
        return self.dirs[self.direction]

    def change_direction(self, other_direction):
        new_direction = (self.direction + other_direction) % 360
        if new_direction < 0:
            new_direction = 360 + new_direction

        self.direction = new_direction

    def rotate_around(self, direction, rotations):
        for _ in range(rotations):
            new_x = self.y * direction
            new_y = self.x * (direction * -1)

            self.x = new_x
            self.y = new_y


north = Position(0, 1, 0)
south = Position(0, -1, 180)

east = Position(1, 0, 90)
west = Position(-1, 0, 270)

cardinal_directions = {
    "N": north,
    "S": south,
    "E": east,
    "W": west
}

change_dir = {"L": -1, "R": 1}


class Ferry:
    def __init__(self):
        self.current_pos = Position(0, 0, 90)

    def __str__(self):
        return str(self.current_pos)

    def move(self, inp: str):
        instruction = split_instr(inp)

        card_dir = instruction[0]
        amount = instruction[1]

        this_postition_obj = cardinal_directions[card_dir]

        change_x = this_postition_obj.x * amount
        change_y = this_postition_obj.y * amount

        change_obj = Position(change_x, change_y, self.current_pos.direction)
        self.current_pos = self.current_pos + change_obj

    def rotate(self, inp: str):
        instruction = split_instr(inp)

        amount = instruction[1]
        direction = change_dir[instruction[0]] * amount
        self.current_pos.change_direction(direction)

    def forward(self, inp: str):
        amount = split_instr(inp)[1]

        direction = self.current_pos.cardinal_dir

        self.move(f"{direction}{amount}")

    def to_waypoint(self, inp, waypoint):
        amount = split_instr(inp)[1]
        self.current_pos.x += waypoint.current_pos.x * amount
        self.current_pos.y += waypoint.current_pos.y * amount


class Waypoint:
    def __init__(self):
        self.current_pos = Position(10, 1)

    def __str__(self):
        return str(self.current_pos)

    def move(self, inp: str):
        instruction = split_instr(inp)

        card_dir = instruction[0]
        amount = instruction[1]

        this_postition_obj = cardinal_directions[card_dir]

        change_x = this_postition_obj.x * amount
        change_y = this_postition_obj.y * amount

        change_obj = Position(change_x, change_y, self.current_pos.direction)
        self.current_pos = self.current_pos + change_obj

    def rotate(self, inp: str):
        instruction = split_instr(inp)

        amount = instruction[1]
        rotations = (int(amount / 360 * 4))
        direction = change_dir[instruction[0]]
        self.current_pos.rotate_around(direction, rotations)


def manhattan_dist(obj_1, obj_2):
    total = obj_1 + obj_2
    return sum((abs(total.x), abs(total.y)))


def part_one():
    this_ferry = Ferry()

    for instr in inputs:
        if instr[0] in cardinal_directions:
            this_ferry.move(instr)

        elif instr[0] in change_dir:
            this_ferry.rotate(instr)

        else:
            this_ferry.forward(instr)

    return manhattan_dist(Position(0, 0), this_ferry.current_pos)


def part_two():
    this_waypoint = Waypoint()
    this_ferry = Ferry()

    for instr in inputs:
        if instr[0] in cardinal_directions:
            this_waypoint.move(instr)

        elif instr[0] in change_dir:
            this_waypoint.rotate(instr)

        else:
            this_ferry.to_waypoint(instr, this_waypoint)

    return manhattan_dist(Position(0, 0), this_ferry.current_pos)


print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")
