with open("5_binary.txt", "r") as f:
    inputs = f.read().split("\n")

mappings = {"B": "1", "F": "0", "R": "1", "L": "0"}

out = [int("".join(mappings[x] for x in each), 2) for each in inputs]

out_len = len(out) + 1
out_min = min(out) - 1

print(out_len * (out_len + 1) // 2 + out_len * out_min - sum(out))
