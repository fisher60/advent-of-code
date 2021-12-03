with open("10_.txt", "r") as f:
    inputs = sorted(list(map(lambda x: int(x), f.read().split("\n"))))

inputs = [0] + inputs + [max(inputs) + 3]

if __name__ == "__main__":
    diff_dict = {1: 0, 2: 0, 3: 0}

    for first, second in zip(inputs, inputs[1:]):
        diff_dict[second - first] += 1

    print(diff_dict[1] * diff_dict[3])
