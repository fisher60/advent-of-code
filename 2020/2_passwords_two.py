with open("2_.txt", "r") as f:
    inputs = f.readlines()

total = 0
for each in inputs:
    each = each.split()
    indexes = list(map(int, each[0].split("-")))
    char = each[1].split(":")[0]
    password = each[2]

    if (password[indexes[0] - 1] == char and password[indexes[1] - 1] != char) or (password[indexes[0] - 1] != char and password[indexes[1] - 1] == char):
        total += 1
        
print(total)