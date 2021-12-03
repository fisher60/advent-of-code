with open("11_.txt", "r") as f:
    inputs = f.read().split("\n")

# with open("11_test.txt", "r") as f:
#     inputs = f.read().split("\n")

checks = [(-1, -1), (-1, 0), (-1, 1),
          (0, 1),
          (1, 1), (1, 0), (1, -1),
          (0, -1)]

empty = "L"
occupied = "#"
floor = "."
x_len = len(inputs[0])
y_len = len(inputs)

are_occupied = {}


def find_seat(position, this_dict):
    out = []
    for check in checks:
        x_pos, y_pos = position
        x_diff, y_diff = check

        while (y_pos, x_pos) in this_dict:
            x_pos += x_diff
            y_pos += y_diff
            if (y_pos, x_pos) in this_dict and this_dict[y_pos, x_pos] in (empty, occupied):
                out.append(this_dict[y_pos, x_pos])
                break
    return out


def part_two():
    check_dict = are_occupied.copy()
    is_complete = True
    for y in range(y_len):
        for x in range(x_len):
            this_seat = are_occupied[y, x]

            adjacent = []
            if this_seat in (empty, occupied):
                adjacent = find_seat((x, y), check_dict)

            if this_seat == occupied and adjacent.count(occupied) >= 5:
                this_swap = empty

            elif this_seat == empty and all([True if x in (floor, empty) else False for x in adjacent]):
                this_swap = occupied
            else:
                continue

            is_complete = False
            are_occupied[y, x] = this_swap

    return is_complete


def part_one():
    check_dict = are_occupied.copy()
    is_complete = True
    for y in range(y_len):
        for x in range(x_len):
            this_seat = are_occupied[y, x]

            adjacent = []
            if this_seat in (empty, occupied):
                for check in checks:
                    y_diff, x_diff = check
                    new_x = x + y_diff
                    new_y = y + x_diff

                    if (new_y, new_x) in check_dict:
                        this_check = check_dict[new_y, new_x]
                    else:
                        this_check = floor

                    adjacent.append(this_check)

            if this_seat == occupied and adjacent.count(occupied) >= 4:
                this_swap = empty

            elif this_seat == empty and all([True if x in (floor, empty) else False for x in adjacent]):
                this_swap = occupied
            else:
                continue

            is_complete = False
            are_occupied[y, x] = this_swap

    return is_complete


def visualize_out(this_data):
    final_sample = []
    start = 0
    end = x_len
    for count in range(y_len):
        final_sample.append("".join(this_data[start:end]))
        start = end
        end += x_len

    return "\n".join(final_sample)


if __name__ == "__main__":
    for row in range(y_len):
        for col in range(x_len):
            are_occupied[row, col] = inputs[row][col]
    complete = False

    while not complete:
        complete = part_two()


    # print(visualize_out(list(are_occupied.values())))

    print(list(are_occupied.values()).count(occupied))
