with open("9_encoding.txt", "r") as f:
    inputs = list(map(lambda x: int(x), f.read().split("\n")))

inputs.reverse()

preamble_len = 25
list_len = len(inputs)


def find_invalid():
    for count, check_num in enumerate(inputs[:-preamble_len]):
        found = False
        look_ahead = preamble_len + count

        available_sums = inputs[count + 1:look_ahead + 1]

        for ind, each in enumerate(available_sums):
            this_sums = available_sums.copy()
            this_sums.remove(each)

            if check_num - each in this_sums:
                found = True
                break

        if not found:
            return check_num, count


def find_combo(number, inde):
    avail_nums = inputs[:inde:-1]
    for i in range(len(avail_nums)):
        out = [avail_nums[i]]
        for count in range(len(avail_nums)):
            this_num = avail_nums[count + i + 1]
            out.append(this_num)
            check_sum = sum(out)
            if check_sum > number:
                break
            elif sum(out) == number:
                return out


if __name__ == "__main__":
    target_num, target_ind = find_invalid()
    seq = find_combo(target_num, target_ind)
    print(min(seq) + max(seq))
