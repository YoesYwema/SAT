import random as r
import numpy as np


def sat_solver(formula, assignment):
    # formula, assignment = tautologies(formula, assignment)
    formula, assignment = pure_literals(clean_formula(formula), assignment)
    formula, assignment = unit_clauses(clean_formula(formula), assignment)
    if formula == - 1:
        return []
    if not formula:
        return assignment
    formula1, formula2, assignment1, assignment2 = split(clean_formula(formula), assignment)
    solution = sat_solver(clean_formula(formula1), assignment1)
    if not solution:
        solution = sat_solver(clean_formula(formula2), assignment2)
    return solution


def tautologies(rules, sudoku):
    return 1


def unit_clauses(formula, assignment):
    unit = []
    for clause in formula:
        if len(clause) == 1:                            # Found a unit clause
            for literal in clause:                      # To get integer instead of list object
                unit.append(literal)                    # Save the unit clause in the list unit
                if literal > 0 and literal not in assignment:    # If literal is positive ..
                    assignment.append(literal)          # Pop clause from formula and add to solution
            clause.clear()
    '''When a unit clause occurs in other clauses or its negation occurs in other clauses'''
    for u in unit:
        for clause in formula:
            if -u in clause:                # When negation of unit clause exists
                clause.remove(-u)           # Remove this negation
                if len(clause) == 0:        # If empty clause this solution is not satisfiable
                    return -1, []
            if u in clause:                 # Occurrence of unit clause
                clause.clear()              # Clause cleared since this one is always true
    formula_cleaned = clean_formula(formula)
    if formula_cleaned == - 1:
        return -1, []
    if not formula_cleaned:
        return formula_cleaned, assignment
    return formula_cleaned, assignment


def pure_literals(formula, assignment):
    seen_literals = list(dict.fromkeys([literal for clause in formula for literal in clause]))      # Get all literals that are in the formula
    pure = list(dict.fromkeys([literal for literal in seen_literals if -literal not in seen_literals])) # Extract the ones that are pure

    for p in pure:
        for clause in formula:
            if p in clause:
                clause.clear()
    for literal in pure:
        if literal > 0:
            assignment.append(literal)
    pure.clear()
    formula_cleaned = clean_formula(formula)
    return formula_cleaned, assignment

def get_random_split_literal(formula):
    # Get all literals
    all_literals = list(dict.fromkeys([literal for clause in formula for literal in clause]))
    # List must contain literals otherwise you'll get an error here
    if all_literals:
        random_literal = r.choice(all_literals)
    return random_literal

def split(formula, assignment):
    formula1 = []
    formula2 = []
    assignment1 = assignment.copy()
    assignment2 = assignment.copy()
    # depends on strategy what you do here: some random literal or some heuristic to get a specific literal
    random_literal = get_random_split_literal(formula)
    if random_literal > 0:                      # Positive literals can be added to the solution
        assignment1.append(random_literal)
    else:
        assignment2.append(-random_literal)     # Means that -random literal is greater then 0
    for clause in formula:
        if random_literal in clause:                # random literal false in formula 2
            formula2.append([literal for literal in clause if literal != random_literal])

        if -random_literal in clause:               # random literal true in formula 1
            formula1.append([literal for literal in clause if literal != -random_literal])
        if random_literal not in clause and -random_literal not in clause:
            formula1.append(clause)
            formula2.append(clause)
    formula1_cleaned = clean_formula(formula1)
    formula2_cleaned = clean_formula(formula2)
    return formula1_cleaned, formula2_cleaned, assignment1, assignment2

'''Prints the solution in a intuitive way'''
def print_sudoku(assignment):
    # create a 2d array with zeroes everywhere
    sudoku = np.zeros((4, 4), dtype=int)
    # take every number in the solution  individually
    for number in assignment:
        number = str(number) # convert the 3 digit number to a string
        sudoku[int(number[1])-1][int(number[2])-1] = number[0]  # first digit -> number, second -> column, third -> row
    print("\nSudoku solution:")
    for j in range(4):
        print(str(sudoku[j]))
    print("\n")


''''Get the clauses with empty lists out of the formula. Lists empty because list remains when you delete a clause'''
def clean_formula(formula):
    if (not formula == -1) or (formula):
        formula = [clause for clause in formula if not clause == []]
    return formula
