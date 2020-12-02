with open("1_fuel_inputs.txt", "r") as f:
    inputs = list(map(int, f.read().split()))


def mass_to_fuel(mass: int) -> int:
    """Given the mass of an object, return the fuel requred to move that object."""
    return mass // 3 - 2


if __name__ == "__main__":
    print(sum(mass_to_fuel(x) for x in inputs))
