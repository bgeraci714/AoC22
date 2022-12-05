def solveA(problem_input):
    count = 0
    for row in problem_input:
        first, second = convert_row_to_pair(row)
        if first[0] <= second[0] and first[1] >= second[1]:
            count += 1
        elif first[0] >= second[0] and first[1] <= second[1]:
            count += 1
    return count


def solveB(problem_input):
    count = 0
    for row in problem_input:
        first, second = convert_row_to_pair(row)
        if is_overlapping(first, second):
            count += 1

    return count


def convert_row_to_pair(row):
    first, second = row.split(',')
    first, second = first.split('-'), second.split('-')
    first = [int(x) for x in first]
    second = [int(x) for x in second]
    return first, second


def is_overlapping(first, second):

    if first[0] == second[0] or first[0] == second[1]:
        # in between second pair of values
        return True
    elif first[1] == second[0] or first[1] == second[1]:
        # in between second pair of values
        return True
    elif second[0] < first[0] < second[1]:
        # within range
        return True
    elif second[0] < first[1] < second[1]:
        # within range
        return True
    elif first[0] <= second[0] <= second[1] <= first[1]:
        return True
    elif second[0] <= first[0] <= first[1] <= second[1]:
        return True

    return False
