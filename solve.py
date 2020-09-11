def solve_sudoku(strategy):
    sudoku = open("fileDimacs", "r").read().splitlines()
    rules = open("sudoku-rules.txt", "r+").read().splitlines()
    """Here we need code to reduce the amount of clauses by the DPLL algorithm """

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

# def tautologies():
#
# def empty_clauses():
#
# def unit_clauses():
#
# def pure_literals():
#
# def amount_of_clauses():
#
# def split():
