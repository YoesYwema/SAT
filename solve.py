def solve_sudoku(strategy):
    sudoku = parser("fileDimacs")
    rules = parser("sudoku-rules.txt")

    if rules == []:
        return True
    for clause in rules:
        if clause == []:
            return False

    #rules, sudoku = tautologies(rules, sudoku)
    rules, sudoku = pure_literals(rules, sudoku)
    #rules, sudoku = unit_clauses(rules,sudoku)

    """Here we need code to reduce the amount of clauses by the DPLL algorithm """

def parser(file):
    clauses = []
    for line in open(file):
        if line.startswith("p"):
            nvars, nclauses = line.split()[2:4]
            continue
        clause = [int(y) for y in line[:-2].split()]
        clauses.append(clause)
    return clauses


# def solve_sudoku_strategy1(strategy):
#     if strategy == 1:  # start solving sudokus with strategy 2
#         print("You've chosen strategy", strategy)
#         solve_sudoku_strategy1()
# def solve_sudoku_strategy2(strategy):
#     if strategy == 2:  # start solving sudokus with strategy 2
#         print("You've chosen strategy", strategy)
#         solve_sudoku_strategy2()
# def solve_sudoku_strategy3(strategy):
#     if strategy == 3:  # start solving sudokus with strategy 3
#         print("You've chosen strategy", strategy)
#         solve_sudoku_strategy3()

def tautologies(rules, sudoku):
    return 1

def unit_clauses(rules, sudoku):
    return 1

def pure_literals(rules, sudoku):
    for literal in sudoku:
        neg_literal = -1*literal

        for line in rules:
            if neg_literal in line:
                line.clear()
                print("removed literals!!")


# def amount_of_clauses():
#
# def split():
