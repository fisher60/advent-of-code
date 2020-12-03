with open("3_.txt", "r") as f:
    inputs = [x.strip("\n") for x in f.readlines()]

if __name__ == "__main__":
    bottom_limit = len(inputs)
    line_len = len(inputs[0])
    x_slopes = [1, 3, 5, 7, 1]
    y_slopes = [1, 1, 1, 1, 2]

    outputs = 1

    for x_slope, y_slope in zip(x_slopes, y_slopes):
        x = y = 0
        trees = 0

        while y < bottom_limit:
            if inputs[y][x] == "#":
                trees += 1

            x = (x + x_slope) % line_len
            y += y_slope

        outputs *= trees

    print(outputs)
