##SAT solver

Project in which we use a satisfiability solver to solve sudokus. You can run the program by giving it the command: 
  
`main.py SAT -S{n} {filename}`

In which `{n}` is the number of the heuristic strategy to get a literal to split the formula (1, 2 or 3). 
**1** for a random literal, **2** for one sided Jeroslaw Wang (JW) and **3** for Maximum Occurrences in clauses of 
Minimum Size (MOMS).


`{filename}` is the name of the file with the sudoku to be solved plus the rules.

The program will print the solved sudoku (if solved) and create a file: `filename.out` in which the slution for 
this sudoku is written in the DIMACS format.