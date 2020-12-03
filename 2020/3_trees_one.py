with open("3_trees.txt", "r") as f:
    inputs = [x.strip("\n") for x in f.readlines()]

if __name__ == "__main__":
    bottom_limit = len(inputs)
    line_len = len(inputs[0])
    trees = 0
    x_slope = 3
    y_slope = 1

    x = y = 0

    while y < bottom_limit:
        if inputs[y][x] == "#":
            trees += 1

        x = (x + x_slope) % line_len
        y += y_slope

    print(trees)
