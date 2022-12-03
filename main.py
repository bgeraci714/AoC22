import os
from pathlib import Path
PROBLEM = 'B'


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def solve(path, input):
    # Use a breakpoint in the code line below to debug your script.
    problem = "A" if "inputA" in path else "B"
    if problem == "A":
        return solveA(input)
    else:
        return solveB(input)


def solveB(input):
    problem_input = input.split("\n")
    totals = []

    total = 0
    for line in problem_input:
        try:
            num = int(line)
            if num == "" or num is None:
                totals.append(total)
                total = 0
            else:
                total += num
        except ValueError:
            totals.append(total)
            total = 0

    totals.sort(reverse=True)
    print(totals[0:3])
    return sum(totals[0:3])


def solveA(input):
    max = -1

    input = input.split("\n")

    sum = 0
    for line in input:
        if (line == ""):
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(line)
    return max


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(os.getcwd())
    # Open function to open the file "MyFile1.txt"
    # (same directory) in append mode and
    path = "problems/1/input" + PROBLEM + ".txt"
    with open(path) as input:
        solution = solve(path, input.read())
        print(solution)
