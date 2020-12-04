with open("4_passport.txt", "r") as f:
    inputs = f.read().split("\n\n")

pass_checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

print(sum(all(x in each for x in pass_checks) for each in inputs))
