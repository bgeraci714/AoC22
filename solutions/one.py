def solveB(problem_input):
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

    sum = 0
    for line in input:
        if (line == ""):
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(line)
    return max