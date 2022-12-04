import os

from solutions.two import solveA, solveB

PROBLEM_PART = 'A'
PROBLEM_NUM = 2


def solve(problem_input):
    # Use a breakpoint in the code line below to debug your script.
    if PROBLEM_PART == "A":
        return solveA(problem_input)
    else:
        return solveB(problem_input)


if __name__ == '__main__':
    print(os.getcwd())
    # Open function to open the file "MyFile1.txt"
    # (same directory) in append mode and
    path = "problems/" + str(PROBLEM_NUM) + "/input.txt"
    with open(path) as input_file:
        solution = solve(input_file.read())
        print(solution)
