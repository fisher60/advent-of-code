def clean_inputs(inp):
    return inp.strip("\n").strip(".").replace("contain ", "").replace(" bags", "").replace(" bag", "").split(",")


with open("7_recursivebags.txt") as f:
    inputs = list(map(clean_inputs, f.readlines()))

dict_map = {}

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


def quantize_child(child):
    return dict_map[child[0]]


def final_count(new_data, match):
    total = 0
    for check in list(new_data):
        if match in new_data[check] and "checked" not in new_data[check]:
            new_data[check].append("checked")
            total += final_count(new_data, check) + 1
    return total


if __name__ == '__main__':
    for chunk in inputs:
        data = format_data(chunk)

        if data[0] not in data_dict:
            data_dict[data[0]] = data[1]
        else:
            data_dict[data[0]] += data[1]

    for count, key in enumerate(data_dict.keys()):
        dict_map[key] = count

    for key, values in data_dict.items():
        mapped_vals = [dict_map[x[0]] for x in values]
        formatted_data[dict_map[key]] = mapped_vals

    print(final_count(formatted_data, dict_map["shiny gold"]))

