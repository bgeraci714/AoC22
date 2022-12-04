import os

from solutions.four import solveA, solveB

PROBLEM_PART = 'B'
PROBLEM_NUM = 4



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
    path = f'problem_inputs/{PROBLEM_NUM}/'

    with open(path + 'sample.txt') as input_file:
        problem_input = input_file.read().split("\n")
        solution = solve(problem_input)
        print(f'sample solution = {solution}')

    with open(path + 'input.txt') as input_file:
        problem_input = input_file.read().split("\n")
        solution = solve(problem_input)
        print(f'problem solution = {solution}')
