from itertools import product

with open("14_.txt", "r") as f:
    inputs = f.read()

# with open("14_test.txt", "r") as f:
#     inputs = f.read()


def clean_inputs(inp):
    inp = inp.split("mask = ")[1:]
    out = {}
    for each in inp:
        temp = each.split("\n")
        key = temp[0]
        values = {}
        for mem in temp[1:]:
            mem = mem.split(" = ")
            if mem != ['']:
                mem_key = mem[0][4: -1]
                mem_val = to_bin(mem[1])
                values[mem_key] = mem_val
        out[key] = values
    return out


def to_bin(num: str):
    this_bin = str(bin(int(num)))[2:]
    return "0" * (36 - len(this_bin)) + this_bin


def part_one(inps):
    total = {}
    for obj in inps:
        mem_dict = inps[obj]
        for mem in mem_dict:
            temp_str = ""
            for swap_char, mem_char in zip(obj, mem_dict[mem]):
                if swap_char != "X":
                    temp_str += swap_char
                else:
                    temp_str += mem_char
            total[mem] = int(temp_str, 2)
    return sum(list(total.values()))


def part_two(inps):
    total = {}

    for obj in inps:
        mem_dict = inps[obj]

        for mem in mem_dict:
            int_temp = int(mem_dict[mem], 2)
            mem = to_bin(mem)
            temp_str = ""
            for swap_char, mem_char in zip(obj, mem):
                if swap_char == "X":
                    temp_str += swap_char
                elif swap_char == "1":
                    temp_str += "1"
                else:
                    temp_str += mem_char

            floating_count = temp_str.count("X")
            poss_ints = [x for x in product(("0", "1"), repeat=floating_count)]
            for combo in poss_ints:
                new_temp_str = ""
                comb_ind = 0
                for char in temp_str:
                    if char == "X":
                        new_temp_str += combo[comb_ind]
                        comb_ind += 1
                    else:
                        new_temp_str += char

                total[new_temp_str] = int(int_temp)
    return sum(list(total.values()))


if __name__ == "__main__":
    cleaned_inputs = clean_inputs(inputs)
    print(f"Solution 1: {part_one(cleaned_inputs)}")
    print(f"Solution 1: {part_two(cleaned_inputs)}")
