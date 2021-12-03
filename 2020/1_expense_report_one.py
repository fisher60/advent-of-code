from functools import reduce
from itertools import combinations

with open("1_expense_report.txt", "r") as f:
    inputs = combinations(map(int, f.read().split()), 2)


def find_matches() -> int:
    """Finds the pair of ints that sum up to 2020, then multiplies them together."""
    for combo in inputs:
        if sum(combo) == 2020:
            return reduce(lambda x, y: x * y, combo)


if __name__ == "__main__":
    print(find_matches())
