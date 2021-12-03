from functools import reduce

with open("16_.txt", "r") as f:
    inputs = f.read().split("\n\n")

# with open("16_test.txt", "r") as f:
#     inputs = f.read().split("\n\n")

all_fields = []
all_tickets = []


class Field:
    def __init__(self, name, lower, upper):
        self.name = name
        self.lower_range = list(range(lower[0], lower[1] + 1))
        self.upper_range = list(range(upper[0], upper[1] + 1))

    def __str__(self):
        return f"Name: {self.name} | Lower: {self.lower_range} | Upper: {self.upper_range}"


class Ticket:
    def __init__(self, sequence):
        self.sequence = [int(x) for x in sequence.split(",")]

    def __str__(self):
        return str(self.sequence)


def clean_inputs(inps):
    raw_fields = inps[0].split("\n")
    nearby_tickets = inps[-1].split("\n")[1:]

    for field in raw_fields:
        temp_field = field.split(": ")
        this_field = temp_field[1].split(" ")

        lower_range = [int(x) for x in this_field[0].split("-")]
        upper_range = [int(x) for x in this_field[-1].split("-")]
        name = temp_field[0]
        all_fields.append(Field(name, lower_range, upper_range))

    for ticket in nearby_tickets:
        all_tickets.append(Ticket(ticket))


def get_your_ticket(inps) -> Ticket:
    this_tick = inps[1].split("your ticket:\n")[-1]
    return Ticket(this_tick)


def part_one():
    invalid_list = []
    for ticket in all_tickets:
        for num in ticket.sequence:
            invalid = True
            for field in all_fields:
                if num in field.lower_range or num in field.upper_range:
                    invalid = False
                    break
            if invalid:
                invalid_list.append(num)

    return sum(invalid_list)


def part_two():
    departure_vals = []
    valid_tickets = []
    poss_fields = {}
    for x in range(len(all_fields)):
        poss_fields[x] = [field.name for field in all_fields]

    for ticket in all_tickets:
        temp_valid = []
        cols_checked = []
        for column, num in enumerate(ticket.sequence):
            for field in all_fields:
                if num in field.lower_range or num in field.upper_range:
                    temp_valid.append((field.name, column))
                    cols_checked.append(column)
        if all(x in cols_checked for x in range(len(ticket.sequence))):
            valid_tickets.append(ticket)

    for val_tick in valid_tickets:
        for ind, val in enumerate(val_tick.sequence):
            for field in all_fields:
                if val in field.lower_range or val in field.upper_range:
                    pass
                else:
                    poss_fields[ind].remove(field.name)

    for field in sorted(poss_fields, key=lambda x: len(poss_fields[x])):
        this_field = next(iter(poss_fields[field]))
        for check_field in poss_fields:
            if field != check_field:
                if this_field in poss_fields[check_field]:
                    poss_fields[check_field].remove(this_field)

    ticket = get_your_ticket(inputs)

    for poss in poss_fields:
        if poss_fields[poss].pop().startswith("departure"):
            departure_vals.append(ticket.sequence[poss])

    return reduce(lambda y, z: y * z, departure_vals)


if __name__ == "__main__":
    clean_inputs(inputs)
    print(f"Solution 1: {part_one()}")
    print(f"Solution 2: {part_two()}")
