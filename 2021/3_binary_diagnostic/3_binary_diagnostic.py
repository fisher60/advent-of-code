with open("3_binary_diagnostic.txt", "r") as f:
    inputs = f.read().split("\n")


def part_1(inps: list):
    gamma = ""
    byte_len = len(inps)
    for position in range(len(inps[0])):
        byte = [x[position] for x in inps]
        if byte.count("1") > byte_len / 2:
            gamma += "1"
        else:
            gamma += "0"
    return int(gamma, 2), int("".join("1" if x == "0" else "0" for x in gamma), base=2)


def check_position_max(inps: list, pos: int) -> list:
    matches = {"1": [], "0": []}
    byte = []
    for line in inps:
        matches[line[pos]].append(line)
        byte.append(line[pos])
    if byte.count("1") >= len(byte) / 2:
        return matches["1"]
    else:
        return matches["0"]


def check_position_min(inps: list, pos: int) -> list:
    matches = {"1": [], "0": []}
    byte = []
    for line in inps:
        matches[line[pos]].append(line)
        byte.append(line[pos])
    if byte.count("1") >= len(byte) / 2:
        return matches["0"]
    else:
        return matches["1"]


def part_2(inps: list):
    max_inps = inps
    min_inps = inps.copy()
    for position in range(len(inps[0])):
        if len(max_inps) > 1:
            max_inps = check_position_max(max_inps, position)
        if len(min_inps) > 1:
            min_inps = check_position_min(min_inps, position)
    return int("".join(max_inps), base=2), int("".join(min_inps), base=2)


if __name__ == '__main__':
    part_1_result = part_1(inputs)
    part_2_result = part_2(inputs)
    print(f"Part One: {part_1_result[0] * part_1_result[1]}")
    print(f"Part Two: {part_2_result[0] * part_2_result[1]}")
