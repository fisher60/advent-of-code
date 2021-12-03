inputs = list(map(int, "13,0,10,12,1,5,8".split(",")))
numbers_said = {}

turn_end_1 = 2020
turn_end_2 = 30000000
inps_len = len(inputs)


def part_one(inps: list, turn_end=2020):
    turn = 0
    next_num = 0  # should not appear until list is consumed
    current_num = inps[0]

    while turn < turn_end:
        if turn < inps_len:
            current_num = inps[turn]
        else:
            current_num = next_num

        if current_num in numbers_said:
            last_said = numbers_said[current_num]
            next_num = turn - last_said
        else:
            next_num = 0

        numbers_said[current_num] = turn
        turn += 1

    return current_num


if __name__ == "__main__":
    sol_1 = part_one(inputs, turn_end=turn_end_1)
    sol_2 = part_one(inputs, turn_end=turn_end_2)
    print(sol_1)
    print(sol_2)
