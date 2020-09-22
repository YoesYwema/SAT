import argparse
import math
import solve

'''Returns sudoku in DIMMACs format'''
def sudoku_into_dimac(file):
    file_dimacs = open("sudoku-dimacs.txt", "w")   # opens new file to write DIMACS version into it
    data = file.read().split()
    size = int(math.sqrt(len(data[0])))     # gives the size of the sudoku
    row = 0
    column = 0
    sudoku_nr = 0
    while sudoku_nr < len(data):  # To make sure you are not going out of bounds in the # of sudokus
        if data[sudoku_nr][(row*size)+column] != '.':
            file_dimacs.write(data[sudoku_nr][(row*size)+column]) # Write down the corresponding number
            file_dimacs.write(str(row+1))               # Write down row number (beginning from 1)
            file_dimacs.write(str(column+1))            # Write down column number (also beginning from 1)
            file_dimacs.write(" 0\n")                   # Write a 0 at the end of the line
        column += 1                     # iterate over columns
        if column >= size:              # if you are further then the last column -> start again one row lower
            column = 0
            row += 1
        if row >= size:                 # if you are further then the last row -> go to the next sudoku
            row = 0
            file_dimacs.write("\n")     # print a new line when going to the next sudoku
            sudoku_nr += 1
    return file_dimacs

'''' Parsing of the arguments into main.py SAT -S{1,2,3} {filename}'''
parser = argparse.ArgumentParser(description="Tell me which strategy to use on which sudokus.")

parser.add_argument("SAT", type=str, nargs='+')

parser.add_argument("--strategy", "-S", type=int, default=1, choices=[1, 2, 3],
                    help="Choose the strategy")

parser.add_argument('inputfile', help="Choose your sudoku file to be solved")

args = parser.parse_args()

''' Parses the rules into clauses without the zeroes'''
def parser(file):
    clauses = []
    for line in open(file):
        if line.startswith("p"):
            nvars, nclauses = line.split()[2:4]
            continue
        clause = [int(y) for y in line[:-2].split()]
        clauses.append(clause)
    return clauses, nvars

''' Parses the given sudoku into clauses without the zeroes'''
def sudoku_parser(file): # now only returns the first sudoku
    clauses = []
    for line in open(file):
        clause = [int(y) for y in line[:-2].split()]
        if clause:
            clauses.append(clause)
        if not clause:
            return clauses


def write_solution_to_file(solution):
    file_solution = open(args.inputfile + ".out", "w")
    for number in solution:
        file_solution.write(str(number) + " 0\n")


''' Reads the sudoku file & calls function to translate sudoku to DIMACS'''
file = open(args.inputfile, "r")
sudoku_into_dimac(file)
file.close()

''' Call to the parsers & call the sat solver in solve.py'''
sudoku = sudoku_parser("sudoku-dimacs.txt")
rules, n_vars = parser("sudoku-rules.txt")
formula = []
formula.extend(rules)
formula.extend(sudoku)
solution = solve.sat_solver(formula, [], 0, 0, args.strategy)

if solution:
    print("Sudoku solution:")
    solve.print_sudoku(list(dict.fromkeys(solution)))
    write_solution_to_file(solution)
else:
    print("Sudoku is unsolvable")
    write_solution_to_file([])
