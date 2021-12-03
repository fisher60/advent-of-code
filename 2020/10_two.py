from functools import lru_cache

with open("10_.txt", "r") as f:
    inputs = sorted(list(map(lambda x: int(x), f.read().split("\n"))))


inputs = (0, *inputs, max(inputs) + 3)


@lru_cache
def calc_perms(new_data):
    total = 1

    if len(new_data) == 1:
        return 0

    if new_data[1] - new_data[0] not in (1, 2, 3):
        return 0

    for ind, num in enumerate(new_data):
        if ind == len(new_data) - 1:
            return total

        if new_data[ind + 1] - num in (1, 2):
            total += calc_perms((num,) + new_data[ind + 2:])

    return total


if __name__ == "__main__":

    print(calc_perms(inputs))
