with open("6_customs.txt", "r") as f:
    inputs = list(map(lambda x: "".join(x.split("\n")), f.read().split("\n\n")))

print(sum(len(set(each)) for each in inputs))
