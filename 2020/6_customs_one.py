with open("6_customs.txt", "r") as f:
    inputs = list(map(lambda x: x.split("\n"), f.read().split("\n\n")))

print(sum(len(set("".join(each))) for each in inputs))
