with open("4_passport.txt", "r") as f:
    inputs = f.read().split("\n\n")


def check_hgt(inp):
    units = {
        "cm": (150, 194),
        "in": (59, 77)
    }

    try:
        hg = int(inp[:-2])
        unit = inp[-2:]

        if unit in ["cm", "in"]:
            check_pass = hg in range(*units[unit])
        else:
            check_pass = False

    except (IndexError, ValueError):
        check_pass = False
    return check_pass


def check_hcl(inp):
    if "#" in inp:
        inp = inp.strip("#")
        good_vals = [str(x) for x in range(10)] + [chr(y) for y in range(ord("a"), ord("f") + 1)]
    else:
        return False
    return len(inp) == 6 and all(x in good_vals for x in inp)


def validate(this_input):
    if all(x in this_input for x in pass_checks):
        each_dict = {x.split(":")[0]: x.split(":")[1] for x in this_input.split()}
        for key, val in each_dict.items():
            if key != "cid":
                if not pass_checks[key](val):
                    return False
    else:
        return False
    return True


pass_checks = {
    "byr": lambda x: int(x) in range(1920, 2003),
    "iyr": lambda x: int(x) in range(2010, 2021),
    "eyr": lambda x: int(x) in range(2020, 2031),
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": lambda x: len(x) == 3 and x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and all(int(y) in range(10) for y in x)
}

if __name__ == "__main__":
    total = 0

    for each in inputs:
        if validate(each):
            total += 1

    print(total)
