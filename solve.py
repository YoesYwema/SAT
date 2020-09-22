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

    if recursion_depth == 1:
        print_sudoku(assignment)

    # Simplification
    formula, pure_assignment = pure_literals(formula)
    formula, unit_assignment = unit_clauses(formula)
    assignment = assignment + pure_assignment + unit_assignment

    # Check if solution found or if failed to find a solution
    if formula == - 1:
        return False
    if not formula:
        return assignment

    # Get random literal to split
    random_literal = get_random_split_literal(formula)
    solution = sat_solver(extract(formula, random_literal), assignment + [random_literal], backtrack, recursion_depth+1)
    if not solution:
        backtrack += 1
        solution = sat_solver(extract(formula, -random_literal), assignment + [-random_literal], backtrack, recursion_depth+1)
    return solution


def tautologies(formula):
    for clause in formula.copy():
        tautologies_list = [literal for literal in clause if -literal in clause and literal > 0]
        if len(tautologies_list) > 0:
            formula.remove(clause)


''' Checks unit literals, removes clauses in which unit literal occurs, removes negation of unit literals from clause'''
def unit_clauses(formula):
    # This is no solution
    if formula == -1:
        return -1, []
    units = []
    # Find unit literals, save them and clear clause if unit literal is in it
    for clause in formula:
        if len(clause) == 1:
            for literal in clause:
                units.append(literal)
    # When a unit clause occurs in other clauses or its negation occurs in other clauses
    units = list(dict.fromkeys(units))
    for unit in units:
        formula = extract(formula, unit)
    return clean_formula(formula), units


''' Checks for pure literals in the formula and removes the clauses in which a pure literal occurs'''
def pure_literals(formula):
    # This is no solution
    if formula == -1:
        return -1, []
    # From all literals that are in the formula extract the ones that occur without their negation
    all_literals = list(dict.fromkeys([literal for clause in formula for literal in clause]))
    pures = list(dict.fromkeys([literal for literal in all_literals if -literal not in all_literals]))
    # Clear all clauses in which a pure literal occurs
    for pure in pures:
        formula = extract(formula, pure)
    return clean_formula(formula), pures


''' Returns a random literal which occurs in formula'''
def get_random_split_literal(formula):
    # Get all positive literals
    all_literals = list(dict.fromkeys([literal for clause in formula for literal in clause if literal > 0]))
    # Choose a literal randomly from all literals
    random_literal = r.choice(all_literals)
    return random_literal


''' Return formula without random literal and -random literal in its clauses (Boolean constraint propagation)'''
def extract(formula, extractable_literal):
    # This is no solution
    if formula == -1:
        return -1
    new_formula = []
    empty_clause = False
    for clause in formula:
        # Random literal set to true, so no need to append to new formula!
        if extractable_literal in clause:
            continue
        # If the opposite of random_literal occurs in a clause append clause except -random_literal
        if -extractable_literal in clause:
            new_formula.append([literal for literal in clause if literal != -extractable_literal])
            if len(clause) == 1:
                empty_clause = True
        # Append clauses to formula if literal or negation does not occur in clause
        if extractable_literal not in clause and -extractable_literal not in clause:
            new_formula.append(clause)
    # If there are empty clauses or the literal does not exist in clauses return -1 (this is no solution)
    if empty_clause:
        return -1
    return new_formula


'''Prints the solution in an intuitive way'''
def print_sudoku(assignment):
    # create a 2d array with zeroes everywhere
    sudoku = np.zeros((9, 9), dtype=int)
    # take every number in the solution  individually
    for number in assignment:
        if number > 0:
            number = str(number) # convert the 3 digit number to a string
            sudoku[int(number[1])-1][int(number[0])-1] = number[2]  # first digit -> number, second -> column, third -> row
    for j in range(9):
        print(str(sudoku[j]))
    print("\n")


''''Get the deleted clauses (which are now empty) out of the formula.'''
def clean_formula(formula):
    if formula == -1:
        return formula
    else:
        formula = [clause for clause in formula if not clause == []]
    return formula
