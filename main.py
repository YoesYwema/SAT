import argparse
parser = argparse.ArgumentParser(description="Tell me which strategy to use on which sudoku.")

parser.add_argument("SAT", type=str, nargs='+')

parser.add_argument("--strategy", "-S", type=int, default=1, choices=[1, 2, 3],
                    help="Choose the strategy")

parser.add_argument('inputfile', help="Choose your sudoku file to be solved")
args = parser.parse_args()

print("Opening file: ", args.inputfile)
file = open(args.inputfile, "r+")     # opens the sudoku file



def sudoku_into_dimac(file, size):
    file_dimacs = open("fileDimacs", "w+")  # write DIMAC version into a new file
    data = file.read().split()
    row = 0
    column = 0
    sudoku_nr = 0

    while data:
        if data[sudoku_nr][(row*9)+column] != '.':
            file_dimacs.write(data[sudoku_nr][(row*9)+column])
            file_dimacs.write(str(row+1))
            file_dimacs.write(str(column+1))
            file_dimacs.write(" 0")
            file_dimacs.write("\n")

        column += 1
        if column >= size:
            column = 0
            row += 1
        if row >= size:
            row = 0
            file_dimacs.write("\n")
            sudoku_nr += 1

    return file_dimacs

size = input("What is the size of the sudoku(s)?\n")
fileDimac = sudoku_into_dimac(file, int(size))

if args.strategy == 1:    # start solving sudokus with strategy 1
    print("You've chosen strategy", args.strategy)
if args.strategy == 2:    # start solving sudokus with strategy 2
    print("You've chosen strategy", args.strategy)
if args.strategy == 3:    # start solving sudokus with strategy 3
    print("You've chosen strategy", args.strategy)
file.close()