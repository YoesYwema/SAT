import argparse
import math
import solve


def sudoku_into_dimac(file):
    file_dimacs = open("fileDimacs", "w")  # opens new file to write DIMAC version into it
    data = file.read().split()
    size = int(math.sqrt(len(data[0])))   # gives the size of the sudoku
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


parser = argparse.ArgumentParser(description="Tell me which strategy to use on which sudokus.")

parser.add_argument("SAT", type=str, nargs='+')

parser.add_argument("--strategy", "-S", type=int, default=1, choices=[1, 2, 3],
                    help="Choose the strategy")

parser.add_argument('inputfile', help="Choose your sudoku file to be solved")
args = parser.parse_args()

print("Opening file: ", args.inputfile)
file = open(args.inputfile, "r")  # opens the sudoku file with the possibility to read the file
sudoku_into_dimac(file)
file.close()
solve.solve_sudoku(args.strategy)

if args.strategy == 1:    # start solving sudokus with strategy 1
    print("You've chosen strategy", args.strategy)

if args.strategy == 2:    # start solving sudokus with strategy 2
    print("You've chosen strategy", args.strategy)
    solve.solve_sudoku_strategy2()
if args.strategy == 3:    # start solving sudokus with strategy 3
    print("You've chosen strategy", args.strategy)
    solve.solve_sudoku_strategy3()
