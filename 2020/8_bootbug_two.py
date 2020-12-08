with open("8_bootbug.txt", "r") as f:
    inputs = f.read().split("\n")


def get_inputs(replace=None):
    out = inputs.copy()
    to_check = split_inp(out[replace])[0]
    if replace is not None and "acc" != to_check:
        if to_check == "nop":
            switch = "jmp"
        else:
            switch = "nop"
        new_inp = (switch, str(split_inp(out[replace])[1]))
        out[replace] = " ".join(new_inp)
    return out


def split_inp(inp):
    inp_split = inp.split(" ")
    return inp_split[0], int(inp_split[1])


def check_results(this_inputs):
    total = 0
    count = 0
    check_dict = {x: False for x in range(len(this_inputs))}

    while not check_dict[count]:
        this_check = split_inp(this_inputs[count])
        check_dict[count] = True

        if this_check[0] == "acc":
            total += this_check[1]
            count += 1
        elif this_check[0] == "jmp":
            count += this_check[1]
        else:
            count += 1

        if count >= len(this_inputs):
            print(total)
            break


if __name__ == "__main__":
    for ind in range(len(inputs)):
        test_inputs = get_inputs(ind)
        check_results(test_inputs)
