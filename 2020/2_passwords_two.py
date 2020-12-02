with open("2_passwords.txt", "r") as f:
    inputs = f.readlines()


class Data:
    def __init__(self, line):
        self.line = line.split()

    @property
    def indexes(self):
        index_1, index_2 = map(int, self.line[0].split("-"))
        return index_1, index_2

    @property
    def char(self):
        return self.line[1].split(":")[0]

    @property
    def password(self):
        return self.line[-1]

    def validate(self):
        checks = [self.password[i - 1] for i in self.indexes]
        return len(set(checks)) > 1 and self.char in checks


if __name__ == "__main__":
    total = 0
    for each in inputs:
        data = Data(each)

        if data.validate():
            total += 1

    print(total)
