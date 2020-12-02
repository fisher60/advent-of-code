with open("2_passwords.txt", "r") as f:
    inputs = f.readlines()


class Data:
    def __init__(self, line):
        self.line = line.split()

    @property
    def lengths(self):
        length_1, length_2 = map(int, self.line[0].split("-"))
        return range(length_1, length_2 + 1)

    @property
    def char(self):
        return self.line[1].split(":")[0]

    @property
    def password(self):
        return self.line[-1]

    def validate(self):
        if self.password.count(self.char) in self.lengths:
            return True
        return False


if __name__ == "__main__":
    total = 0

    for each in inputs:
        data = Data(each)
        if data.validate():
            total += 1

    print(total)
