import os

from solutions.six import solve_a, solve_b

PROBLEM_PART = 'B'
PROBLEM_NUM = 6


def solve(parsed_input):
    # Use a breakpoint in the code line below to debug your script.
    if PROBLEM_PART == "A":
        return solve_a(parsed_input)
    else:
        return solve_b(parsed_input)


if __name__ == '__main__':
    print(os.getcwd())
    path = f'problem_inputs/{PROBLEM_NUM}/'

    with open(path + 'sample.txt') as input_file:
        problem_input = input_file.read().split("\n")
        solution = solve(problem_input)
        print(f'sample solution = {solution}')

    with open(path + 'input.txt') as input_file:
        problem_input = input_file.read().split("\n")
        solution = solve(problem_input)
        print(f'problem solution = {solution}')
