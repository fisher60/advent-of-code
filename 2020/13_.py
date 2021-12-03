from functools import reduce

with open("13_.txt", "r") as f:
    inputs = f.read().split("\n")

# with open("13_test.txt", "r") as f:
#     inputs = f.read().split("\n")


def clean_inp(inp):
    return [int(x) for x in inp.split(",") if x not in ("x", ",")]


def clean_subsequent_inps(inp):
    return inp.split(",")

min_delta = int(inputs[0])
bus_deltas = clean_inp(inputs[1])

bus_time_checks = clean_subsequent_inps(inputs[1])

print(bus_time_checks)


def part_one():
    count = min_delta
    check_deltas = {}
    while len(check_deltas) < 1:
        for bus in bus_deltas:
            if not count % bus:
                check_deltas[count] = bus
        count += 1


    min_time = min(check_deltas)
    return (min_time - min_delta) * check_deltas[min_time]


def get_inverse(a, b):
    if a == 0:
        return 0
    else:
        if not b % a:
            return 1
        else:
            return b - get_inverse(b % a, a) * b // a


def part_two():
    prod = reduce(lambda x, y: x * y, bus_deltas)
    total = 0
    for count, each in enumerate(bus_time_checks):
        if each != "x":
            each = int(each)
            this = count * (prod // each) * get_inverse(prod // each, each)
            total += this
    return prod - total % prod



if __name__ == "__main__":
    # print(part_one())
    print(part_two())