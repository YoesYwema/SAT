import random as r
import numpy as np


def sat_solver(formula, assignment, satisfiable):
    print(formula)
    if not formula:
        satisfiable = True
        return assignment, satisfiable

    # formula, assignment = tautologies(formula, assignment)
    formula, assignment = unit_clauses(formula, assignment)
    formula, assignment = pure_literals(formula, assignment)
    formula1, formula2, assignment1, assignment2 = split(formula, assignment)
    sat_solver(formula1, assignment1, satisfiable)
    sat_solver(formula2, assignment2, satisfiable)


def tautologies(rules, sudoku):
    return 1


def unit_clauses(formula, assignment):
    unit = []
    for clause in formula:
        if len(clause) == 1:                            # Found a unit clause
            for literal in clause:                      # To get integer instead of list object
                unit.append(literal)                    # Save the unit clause in the list unit
                if literal > 0:                         # If literal is positive ..
                    assignment.append(literal)          # Pop clause from formula and add to solution
                    clause.pop()
    '''When a unit clause occurs in other clauses or its negation occurs in other clauses'''
    for clause in formula:
        for u in unit:
            for literal in clause:
                if u == literal:                # Occurrence of unit clause
                    clause.pop()                # Clause deleted since this one is always true
                if -u == literal:               # When negation of unit clause exists
                    clause.remove(literal)      # Remove this negation
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


def split(formula, assignment):
    formula1 = []
    formula2 = []
    assignment1 = assignment2 = assignment
    # depends on strategy what you do here: some random literal or some heuristic to get a specific literal
    random_literal = r.choice(list(dict.fromkeys([literal for clause in formula for literal in clause])))
    formula1.append([random_literal])
    formula2.append([-random_literal])

    if random_literal > 0:
        assignment1.append(random_literal)
    if -random_literal > 0:
        assignment2.append(-random_literal)

    for clause in formula:
        if random_literal in clause:
            formula1.append(clause)
        if -random_literal in clause:
            formula2.append(clause)
        if random_literal not in clause and -random_literal not in clause:
            formula1.append(clause)
            formula2.append(clause)

    return formula1, formula2, assignment1, assignment2


def print_sudoku(assignment):
    # create a 2d array with zeroes everywhere
    sudoku = np.zeros((9, 9), dtype=int)
    # take every number in the solution  individually
    print(assignment)
    for number in assignment:
        number = str(number) # convert the 3 digit number to a string
        sudoku[int(number[1])-1][int(number[2])-1] = number[0] # first digit is the number, second the column nad third the row
    print("\nSudoku solution:")
    for j in range(9):
        print(str(sudoku[j]))
    print("\n")


