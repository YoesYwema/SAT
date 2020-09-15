def sat_solver(formula, assignment, satisfiable):
    if not formula:
        satisfiable = True
    for clause in formula:
        if not clause:
            satisfiable = False

    # formula, assignment = tautologies(formula, assignment)

    formula, assignment = unit_clauses(formula, assignment)
    print("Assignment: " + str(assignment))
    print("Formula: " + str(formula))

    formula, assignment = pure_literals(formula, assignment)
    print("Assignment: " + str(assignment))
    print("Formula: " + str(formula))

    # formula1, formula2, assignment = split(formula, assignment)

    # sat_solver(formula1, assignment, False)
    # sat_solver(formula2, assignment, False)
    # print("Assignment: " + str(assignment))

    return assignment, satisfiable

def tautologies(rules, sudoku):
    return 1


def unit_clauses(formula, assignment):
    unit = []
    for clause in formula:
        if len(clause) == 1:                        # Found a unit clause
            for literal in clause:
                unit.append(literal)                # Save the unit clauses
            if literal > 0:                         # If literal is positive ..
                assignment.append(clause.pop())     # Add literal to the solution and delete clause from formula
    for clause in formula:
        i = 0
        while i < len(unit):
            for literal in clause:
                if unit[i] == literal:              # Occurrence of unit clause
                    clause.clear()                  # Clause deleted since this one is always true
                if -unit[i] == literal:             # When negation of unit clause exists
                    clause.remove(literal)          # Remove this negation from all other clauses
            i += 1
    return formula, assignment


def pure_literals(formula, assignment):
    seen_literals = list(dict.fromkeys([literal for clause in formula for literal in clause]))      # Get all literals that are in the formula
    pure = list(dict.fromkeys([literal for literal in seen_literals if -literal not in seen_literals])) # Extract the ones that are pure

    i = 0
    while i < len(pure):
        for clause in formula:
            for literal in clause:
                if literal in pure:
                    clause.pop()
            i += 1

    for item in pure:
        if item > 0:
            assignment.append(item)
    pure.clear()
    return formula, assignment

# def split():
