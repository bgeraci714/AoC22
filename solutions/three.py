from string import ascii_lowercase, ascii_uppercase
from math import floor

def solveA(problem_input):
    char_values = build_char_values()
    sum = 0
    for line in problem_input:

        mid = floor(len(line) / 2)
        print(mid)
        comp1, comp2 = line[0:mid], line[mid:]
        print(comp1, comp2)

        seen = set()
        for item in comp1:
            seen.add(item)

        for item in comp2:
            if item in seen:
                print(item)
                sum += char_values[item]
                break

    return sum


def solveB(problem_input):
    char_values = build_char_values()
    sum = 0
    for group in chunks(problem_input, 3):
        sack1, sack2, sack3 = group
        for item in sack3:
            if item in sack1 and item in sack2:
                print(item)
                sum += char_values[item]
                break

    return sum



def build_char_values():
    char_values = dict()

    count = 1
    for letter in ascii_lowercase:
        char_values[letter] = count
        count += 1

    for letter in ascii_uppercase:
        char_values[letter] = count
        count += 1

    return char_values

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]