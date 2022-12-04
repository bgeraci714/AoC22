def solveA(problem_input):
    count = 0
    for pair in problem_input:
        first, second = pair.split(',')
        first, second = first.split('-'), second.split('-')
        if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
            count += 1
        elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
            count += 1
    return count

def solveB(problem_input):
    count = 0
    for pair in problem_input:
        first, second = pair.split(',')
        first, second = first.split('-'), second.split('-')
        if int(first[0]) <= int(second[0]) or int(first[1]) >= int(second[1]):
            count += 1
        elif int(first[0]) >= int(second[0]) or int(first[1]) <= int(second[1]):
            count += 1
    return count