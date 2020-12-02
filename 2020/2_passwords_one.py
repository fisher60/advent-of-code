with open("2_.txt", "r") as f:
    inputs = f.readlines()

total = 0

for each in inputs:
    each = each.split()
    lengths = list(map(int, each[0].split("-")))
    lengths = list(range(lengths[0], lengths[1] + 1))
    char = each[1].split(":")[0]
    password = each[2]
    if password.count(char) in lengths:
        total += 1

print(total)
