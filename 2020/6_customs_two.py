with open("6_customs.txt", "r") as f:
    inputs = list(map(lambda x: x.split("\n"), f.read().split("\n\n")))

total = 0

reset_table = {chr(x): False for x in range(ord("a"), ord("z") + 1)}

for each in inputs:
    group_size = len(each)
    checked = reset_table.copy()
    this_sum = 0
    answers = "".join(each)

    for char in answers:
        if answers.count(char) == group_size and not checked[char]:
            checked[char] = True
            this_sum += 1

    total += this_sum

print(total)
