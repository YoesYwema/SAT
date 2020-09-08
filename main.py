import argparse
parser = argparse.ArgumentParser(description="Tell me which strategy to use on which sudoku.")

parser.add_argument("SAT", type=str, nargs='+')

parser.add_argument("--strategy", "-S", type=int, default=1, choices=[1, 2, 3],
                    help="Choose the strategy")

parser.add_argument('inputfile', help="Choose your sudoku file to be solved")
args = parser.parse_args()

print("Opening file: ", args.inputfile)
file = open(args.inputfile, "r+")     # opens the sudoku file

def sudoku_into_dimac(file):
    fileDimacs = open("fileD", "w+")  # write DIMAC version into a new file
    """"Needs code to translate sudoku into DIMACS format  """
    return fileDimacs


fileDimac = sudoku_into_dimac(file)
if args.strategy == 1:    # start solving sudokus with strategy 1
    print("You've chosen strategy", args.strategy)
if args.strategy == 2:    # start solving sudokus with strategy 2
    print("You've chosen strategy", args.strategy)
if args.strategy == 3:    # start solving sudokus with strategy 3
    print("You've chosen strategy", args.strategy)
file.close()