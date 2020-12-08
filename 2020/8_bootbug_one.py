with open("8_bootbug.txt", "r") as f:
    inputs = list(map(lambda x: x.replace("+", ""), f.read().split("\n")))


def split_inp(inp):
    inp_split = inp.split(" ")
    return inp_split[0], int(inp_split[1])


if __name__ == "__main__":
    total = 0
    count = 0
    offset = 0
    check_dict = {x: False for x in range(len(inputs))}

    while not check_dict[count + offset]:
        this_check = split_inp(inputs[count + offset])

        if this_check[0] == "acc":
            total += this_check[1]
        elif this_check[0] == "jmp":
            offset += this_check[1]
            continue

        check_dict[count + offset] = True

        count += 1

    print(total)
