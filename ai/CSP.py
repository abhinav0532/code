domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

constraints = {
    ('A', 'B'): lambda a, b: a > b,
    ('B', 'A'): lambda b, a: b < a,
    ('B', 'C'): lambda b, c: b == c,
    ('C', 'B'): lambda c, b: c == b,
}

def revise(x, y):

    revised = False

    x_domain = domains[x]
    y_domain = domains[y]

    all_constraints = [
        constraint for constraint in constraints if constraint[0] == x and constraint[1] == y]

    for x_value in x_domain:
        satisfies = False
        for y_value in y_domain:
            for constraint in all_constraints:
                constraint_func = constraints[constraint]
                if constraint_func(x_value, y_value):
                    satisfies = True
        if not satisfies:
            x_domain.remove(x_value)
            revised = True

    return revised


def ac3(arcs):
    queue = arcs[:]

    while queue:
        (x, y) = queue.pop(0)

        revised = revise(x, y)

        if revised:
            neighbors = [neighbor for neighbor in arcs if neighbor[1] == x]
            queue = queue + neighbors


arcs = [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B')]
ac3(arcs)
print(domains)