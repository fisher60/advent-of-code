with open("1_fuel_inputs.txt", "r") as f:
    inputs = list(map(int, f.read().split()))


def mass_to_fuel(mass: int) -> int:
    """
    Given the mass of an object, returns the fuel required to move that object
    as well as the additional fuel to move that fuel.
    """

    fuel_to_add = mass // 3 - 2
    total_fuel = fuel_to_add

    while fuel_to_add > 0:
        fuel_to_add = fuel_to_add // 3 - 2

        if fuel_to_add > 0:
            total_fuel += fuel_to_add
        else:
            return total_fuel


if __name__ == "__main__":
    print(sum(mass_to_fuel(x) for x in inputs))
