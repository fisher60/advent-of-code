from typing import Optional

with open("1_sonar_sweep_inputs.txt", "r") as f:
    inps = list(map(int, f.read().split("\n")))


def solution(numbers: list, chunk_size: Optional[int] = 1) -> int:
    """
    Return the count where the next element in the iterable is greater than the previous.

    Chunk size is the number of elements to sum/check, works with either 1 or 3.
    """
    return sum(second > first for first, second in zip(numbers, numbers[chunk_size:]))


if __name__ == "__main__":
    print(f"Part One: {solution(inps)}")
    print(f"Part Two: {solution(inps, chunk_size=3)}")
