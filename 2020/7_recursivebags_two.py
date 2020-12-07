def clean_inputs(inp):
    return inp.strip("\n").strip(".").replace("contain ", "").replace(" bags", "").replace(" bag", "").split(",")


with open("7_recursivebags.txt") as f:
    inputs = list(map(clean_inputs, f.readlines()))

data_dict = {}

formatted_data = {}


def get_bag(inp) -> tuple:
    return inp[2:], inp[0]


def format_data(inp):
    contains = []
    this_bag = None

    for each in inp:
        if each[0] == " ":
            each = each[1:]

        if each[0].isdigit():
            contains.append(get_bag(each))

        else:
            if "no other" in each:
                this_bag = each.split(" no other")[0]

            else:
                for ind, char in enumerate(each):
                    if char.isdigit():
                        this_bag = each[:ind - 1]
                        contains.append(get_bag(each[ind:]))
                        break

    return this_bag, contains


def final_count(new_data, match):
    total = 0
    if len(new_data[match]):
        for bag in new_data[match]:
            total += int(bag[1]) * (final_count(new_data, bag[0]) + 1)
    return total


if __name__ == '__main__':
    for chunk in inputs:
        data = format_data(chunk)

        if data[0] not in data_dict:
            data_dict[data[0]] = data[1]
        else:
            data_dict[data[0]] += data[1]

    print(final_count(data_dict, "shiny gold"))
