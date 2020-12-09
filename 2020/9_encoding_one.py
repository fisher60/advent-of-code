with open("9_encoding.txt", "r") as f:
    inputs = list(map(lambda x: int(x), f.read().split("\n")))

inputs.reverse()

preamble_len = 25
list_len = len(inputs)


if __name__ == "__main__":
    for count, check_num in enumerate(inputs[:-preamble_len]):
        found = False
        look_ahead = preamble_len + count

        available_sums = inputs[count + 1:look_ahead + 1]

        for ind, each in enumerate(available_sums):
            this_sums = available_sums.copy()
            this_sums.remove(each)

            if check_num - each in this_sums:
                found = True
                break

        if not found:
            print("FOUND INVALID")
            print(check_num)
