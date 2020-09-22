import random as r
import numpy as np


def sat_solver(formula, assignment, backtrack, tree_height):
    if formula == - 1:
        return False
    if not formula:
        return assignment

    tree_height += 1
    if tree_height == 1:
        tautologies(formula)

    formula, pure_assignment = pure_literals(clean_formula(formula))
    formula, unit_assignment = unit_clauses(clean_formula(formula))
    assignment = assignment + pure_assignment + unit_assignment

    if formula == - 1:
        return False
    if not formula:
        return assignment

    # print("Assignment after simplification is: ", str(assignment))
    random_literal = get_random_split_literal(formula)
    print("Random literal to split assignment:", str(random_literal))
    solution = sat_solver(try_literal(clean_formula(formula), random_literal), assignment + [random_literal], backtrack, tree_height)
    if not solution:
        print("Backtrack and try counter example")
        backtrack += 1
        print("Amount of times backtracked: ", str(backtrack))
        solution = sat_solver(try_literal(clean_formula(formula), -random_literal), assignment + [-random_literal], backtrack, tree_height)
        # print("Solution (post) is: ", str(solution))
    return solution


def tautologies(formula):
    for clause in formula.copy():
        clause_duplicates = [literal for literal in clause if (literal * -1) in clause and literal > 0]
        if len(clause_duplicates) > 0:
            formula.remove(clause)


def unit_clauses(formula):
    #print("At the begin formula is: ", str(clean_formula(formula)))
    if formula == -1:
        return -1, []
    formula_copy = formula.copy()
    unit = []
    assignment = []
    for clause in formula_copy:
        if len(clause) == 1:                            # Found a unit clause
            for literal in clause:                      # To get integer instead of list object
                unit.append(literal)                    # Save the unit clause in the list unit
            clause.clear()
    '''When a unit clause occurs in other clauses or its negation occurs in other clauses'''
    for u in unit:
        for clause in formula_copy:
            if -u in clause:                # When negation of unit clause exists
                clause.remove(-u)           # Remove this negation
                if len(clause) == 0:        # If empty clause this solution is not satisfiable
                    return -1, []
            if u in clause:                 # Occurrence of unit clause
                clause.clear()              # Clause cleared since this one is always true
    print("Found unit clauses: ", list(dict.fromkeys(unit)))
    #print("Afterwards formula is: ", str(clean_formula(formula)))
    assignment += list(dict.fromkeys(unit))
    return clean_formula(formula_copy), assignment


def pure_literals(formula):
    if formula == -1:
        return -1, []
    formula_copy = formula.copy()
    assignment = []
    seen_literals = list(dict.fromkeys([literal for clause in formula_copy for literal in clause]))      # Get all literals that are in the formula
    pure = list(dict.fromkeys([literal for literal in seen_literals if -literal not in seen_literals])) # Extract the ones that are pure
    #print("At the begin formula is: ", str(formula))
    print("Found pures: ", str(pure))
    for p in pure:
        for clause in formula_copy:
            if p in clause:
                clause.clear()
    assignment += list(dict.fromkeys(pure))
    #print("Afterwards formula is: ", str(clean_formula(formula)))
    return clean_formula(formula_copy), assignment


def get_random_split_literal(formula):
    # Get all literals
    all_literals = list(dict.fromkeys([literal for clause in formula for literal in clause]))
    random_literal = r.choice(all_literals)
    return random_literal


def try_literal(formula, random_literal):
    new_formula = []
    empty_clause = False
    counter = 0
    for clause in formula:
        # Delete literals from clause because they cannot be true anymore
        if -random_literal in clause:
            new_formula.append([literal for literal in clause if literal != -random_literal])
            if len(clause) == 1:
                empty_clause = True
        # Append clauses to formula if literal or negation does not occur in clause
        if random_literal not in clause and -random_literal not in clause:
            new_formula.append(clause)
        # Clause is true so do not append to new formula
        if random_literal in clause:
            counter += 1
            continue
    if empty_clause or counter == 0:
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


''''Get the clauses with empty lists out of the formula. Lists empty because list remains when you delete a clause'''
def clean_formula(formula):
    if formula == -1:
        return formula
    else:
        formula = [clause for clause in formula if not clause == []]
    return formula
