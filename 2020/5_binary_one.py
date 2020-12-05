with open("5_binary.txt", "r") as f:
    inputs = f.read().split("\n")

mappings = {"B": "1", "F": "0", "R": "1", "L": "0"}

print(max(int("".join(mappings[x] for x in each), 2) for each in inputs))
