def solve_sudoku(strategy):
    sudoku = sudoku_parser("fileDimacs")
    rules, n_vars = parser("sudoku-rules.txt")
    formula = rules.append(sudoku)
    solution = []

    if not formula:             # No more clauses so the problem is solved
        return True, solution
    for clause in formula:      # There exist an Empty clause so problem is unsatisfiable
        if not clause:
            return False

    # formula, solution  = tautologies(formula, solution)

    formula, solution = pure_literals(formula, solution)

    # formula, solution = unit_clauses(formula, solution)

    # formula, solution = split(formula, solution)


    """Here we need code to reduce the amount of clauses by the DPLL algorithm """

def parser(file):
    clauses = []
    for line in open(file):
        if line.startswith("p"):
            nvars, nclauses = line.split()[2:4]
            continue
        clause = [int(y) for y in line[:-2].split()]
        clauses.append(clause)
    return clauses, nvars


def sudoku_parser(file): # now only gives the first sudoku
    clauses = []
    for line in open(file):
        clause = [int(y) for y in line[:-2].split()]
        if clause:
            clauses.append(clause)
        if not clause:
            return clauses



def tautologies(rules, sudoku):
    return 1

def unit_clauses(rules, sudoku):
    return 1

def pure_literals(rules, sudoku):
    for literal in sudoku:
        neg_literal = -1*literal
        for line in rules:
            if line == literal:
                line.clear()
                print("cleared line!")
            if line == neg_literal:
                line.remove(literal)
                print("removed literals!")
    return rules, sudoku

# def amount_of_clauses():
#
# def split():
