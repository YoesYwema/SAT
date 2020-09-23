import random as r

'''Main function that is called recursively to perform DPLL algorithm'''
def sat_solver(formula, assignment, backtrack, recursion_depth, strategy):
    # Check if solution found or if failed to find a solution
    if formula == - 1:
        return False
    if not formula:
        return assignment
    # Only check for tautologies the first time
    if recursion_depth == 0:
        tautologies(formula)

    # Simplification
    formula, assignment = pure_literals(formula, assignment)
    formula, assignment = unit_clauses(formula, assignment)

    # Check if solution found or if failed to find a solution
    if formula == - 1:
        return False
    if not formula:
        return assignment

    # Use chosen heuristic
    if strategy == 1:  # Random
        split_literal = get_random_split_literal(formula)
    if strategy == 2:  # One sided Jeroslaw Wang (JW)
        split_literal = get_random_split_literal(formula)
        '''Instead of random literal you can implement heuristic here'''
    if strategy == 3:  # Maximum Occurrences in clause of Minimum Size (MOMS)
        split_literal = get_random_split_literal(formula)
        '''Instead of random literal you can implement heuristic here'''

    solution = sat_solver(delete(formula, split_literal), assignment + [split_literal], backtrack, recursion_depth+1, strategy)
    if not solution:
        backtrack += 1
        solution = sat_solver(delete(formula, -split_literal), assignment + [-split_literal], backtrack, recursion_depth+1, strategy)
    return solution


''' Checks and deletes tautologies (although they do not appear in the sudoku's)'''
def tautologies(formula):
    for clause in formula:
        tautologies_list = [literal for literal in clause if -literal in clause and literal in clause]
        if len(tautologies_list) > 0:
            formula.remove(clause)


''' Checks unit literals, removes clauses in which unit literal occurs, removes negation of unit literals from clause'''
def unit_clauses(formula, assignment):
    # This is no solution
    if formula == -1:
        return -1, []
    units = []
    # Find unit literals and save them
    for clause in formula:
        if len(clause) == 1:
            for literal in clause:
                units.append(literal)
    # When a unit clause occurs in other clauses or its negation occurs in other clauses
    units = list(dict.fromkeys(units))
    assignment += units
    for unit in units:
        formula = delete(formula, unit)
    return formula, assignment


''' Checks for pure literals in the formula and removes the clauses in which a pure literal occurs'''
def pure_literals(formula, assignment):
    # This is no solution
    if formula == -1:
        return -1, []
    # From all literals that are in the formula extract the ones that occur without their negation
    all_literals = list(dict.fromkeys([literal for clause in formula for literal in clause]))
    pures = list(dict.fromkeys([literal for literal in all_literals if -literal not in all_literals]))
    assignment += pures
    # Clear all clauses in which a pure literal occurs
    for pure in pures:
        formula = delete(formula, pure)
    return formula, assignment


''' Returns a random literal which occurs in formula'''
def get_random_split_literal(formula):
    # Get all positive literals
    all_literals = list(dict.fromkeys([literal for clause in formula for literal in clause if literal > 0]))
    # Choose a literal randomly from all literals
    if len(all_literals) > 0:
        random_literal = r.choice(all_literals)
    else:
        return -1
    return random_literal


''' Return formula without random literal and -random literal in its clauses (Boolean constraint propagation)'''
def delete(formula, extractable_literal):
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
