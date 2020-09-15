def solve_sudoku(strategy):
    sudoku = sudoku_parser("fileDimacs")
    rules, n_vars = parser("sudoku-rules.txt")
    formula = []
    formula.extend(rules)
    formula.extend(sudoku)
    assignment = []

    # formula, solution  = tautologies(formula, assignment)

    # formula, solution = pure_literals(formula, assignment)

    formula, solution = unit_clauses(formula, assignment)

    # formula, solution = split(formula, assignment)


    """Here we need code to reduce the amount of clauses by the DPLL algorithm """

def parser(file): # parses the rules into clauses without the zeroes
    clauses = []
    for line in open(file):
        if line.startswith("p"):
            nvars, nclauses = line.split()[2:4]
            continue
        clause = [int(y) for y in line[:-2].split()]
        clauses.append(clause)
    return clauses, nvars


def sudoku_parser(file): # now only returns the first sudoku
    clauses = []
    for line in open(file):
        clause = [int(y) for y in line[:-2].split()]
        if clause:
            clauses.append(clause)
        if not clause:
            return clauses


def tautologies(rules, sudoku):
    return 1


def unit_clauses(formula, assignment):
    unit = []
    for clause in formula:
        if len(clause) == 1:                    # Found a unit clause
            for i in clause:
                unit.append(i)                  # Save the unit clauses
            assignment.append(clause.pop())     # Add unit clause to the solution and delete clause from formula
    for clause in formula:
        i = 0
        while i < len(unit):
            for literal in clause:
                if -unit[i] == literal:         # When negation of unit clause exists
                    clause.remove(literal)      # Remove this negation from all other clauses
            i += 1
    return formula, assignment



# def pure_literals(formula, solution):
#
# def amount_of_clauses():
#
# def split():
