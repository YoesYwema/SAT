import random as r
import numpy as np


def sat_solver(formula, assignment, backtrack, recursion_depth):
    # Check if solution found or if failed to find a solution
    if formula == - 1:
        return False
    if not formula:
        return assignment

    # Only check for tautologies the first time
    if recursion_depth == 0:
        tautologies(formula)
    print("Recursion depth: ", str(recursion_depth))

    # Simplification
    print("Simplification")
    formula, pure_assignment = pure_literals(clean_formula(formula))
    formula, unit_assignment = unit_clauses(clean_formula(formula))
    assignment = assignment + pure_assignment + unit_assignment

    # Check if solution found or if failed to find a solution
    if formula == - 1:
        return False
    if not formula:
        return assignment

    # Get random literal to split
    random_literal = get_random_split_literal(formula)
    print("Split(1) ", str(random_literal))
    solution = sat_solver(extract(clean_formula(formula), random_literal), assignment + [random_literal], backtrack, recursion_depth+1)
    if not solution:
        backtrack += 1
        print("Split(2) ", str(-random_literal))
        solution = sat_solver(extract(clean_formula(formula), -random_literal), assignment + [-random_literal], backtrack, recursion_depth+1)
    return solution


def tautologies(formula):
    for clause in formula.copy():
        clause_duplicates = [literal for literal in clause if (literal * -1) in clause and literal > 0]
        if len(clause_duplicates) > 0:
            formula.remove(clause)


''' Checks for unit literals and removes clauses in which unit literal occurs, also removes the negation of the unit literals  from clauses'''
def unit_clauses(formula):
    # This is no solution
    if formula == -1:
        return -1, []
    formula_copy = formula.copy()
    units = []
    # Find unit literals, save them and clear clause if unit literal is in it
    for clause in formula_copy:
        if len(clause) == 1:
            for literal in clause:
                units.append(literal)
            clause.clear()
    # When a unit clause occurs in other clauses or its negation occurs in other clauses
    for unit in units:
        for clause in formula_copy:
            if -unit in clause:                # When negation of unit clause exists
                clause.remove(-unit)           # Remove this negation
                if len(clause) == 0:        # If empty clause this solution is not satisfiable
                    print("Found empty clause by unit clause elimination")
                    return -1, []
            if unit in clause:                 # Occurrence of unit clause
                clause.clear()              # Clause cleared since this one is always true
    units = list(dict.fromkeys(units))
    return clean_formula(formula_copy), units


''' Checks for pure literals in the formula and removes the clauses in which a pure literal occurs'''
def pure_literals(formula):
    # This is no solution
    if formula == -1:
        return -1, []
    formula_copy = formula.copy()
    # From all literals that are in the formula extract the ones that occur without their negation
    all_literals = list(dict.fromkeys([literal for clause in formula_copy for literal in clause]))
    pure = list(dict.fromkeys([literal for literal in all_literals if -literal not in all_literals]))
    # Clear all clauses in which a pure literal occurs
    for p in pure:
        for clause in formula_copy:
            if p in clause:
                clause.clear()
    return clean_formula(formula_copy), pure

''' Returns a random literal which occurs in formula'''
def get_random_split_literal(formula):
    # Get all literals
    all_literals = list(dict.fromkeys([literal for clause in formula for literal in clause]))
    # Choose a literal randomly from all literals
    random_literal = r.choice(all_literals)
    return random_literal


''' Return formula without random literal and -random literal in its clauses (Boolean constraint propagation)'''
def extract(formula, random_literal):
    new_formula = []
    empty_clause = False
    counter = 0
    for clause in formula:
        # Random literal set to true, so no need to append to new formula!
        if random_literal in clause:
            counter += 1
            continue
        # If the opposite of random_literal occurs in a clause append clause except -random_literal
        if -random_literal in clause:
            new_formula.append([literal for literal in clause if literal != -random_literal])
            if len(clause) == 1:
                empty_clause = True
        # Append clauses to formula if literal or negation does not occur in clause
        if random_literal not in clause and -random_literal not in clause:
            new_formula.append(clause)
    # If there are empty clauses or the literal does not exist in clauses return -1 (this is no solution)
    if empty_clause or counter == 0:
        print("Found empty clause by split literal")
        return -1
    return new_formula


'''Prints the solution in an intuitive way'''
def print_sudoku(assignment):
    # create a 2d array with zeroes everywhere
    sudoku = np.zeros((4, 4), dtype=int)
    # take every number in the solution  individually
    for number in assignment:
        if number > 0:
            number = str(number) # convert the 3 digit number to a string
            sudoku[int(number[1])-1][int(number[2])-1] = number[0]  # first digit -> number, second -> column, third -> row
    print("\nSudoku solution:")
    for j in range(4):
        print(str(sudoku[j]))
    print("\n")


''''Get the deleted clauses (which are now empty) out of the formula.'''
def clean_formula(formula):
    if formula == -1:
        return formula
    else:
        formula = [clause for clause in formula if not clause == []]
    return formula
