def solve_a(problem_input):
    unique_signal_size = 4
    solutions = []
    for signal in problem_input:
        solution = find_first_unique_set(signal, unique_signal_size)
        solutions.append(solution)
    return solutions


def solve_b(problem_input):
    unique_signal_size = 14
    solutions = []
    for signal in problem_input:
        solution = find_first_unique_set(signal, unique_signal_size)
        solutions.append(solution)
    return solutions


def find_first_unique_set(signal, chunk_size):
    for chunk, idx in chunks(signal, chunk_size):
        if is_unique(chunk):
            return idx

    return -1


def is_unique(chunk):
    seen = set()
    for char in chunk:
        if char in seen:
            return False
        seen.add(char)
    return True


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst)):
        yield lst[i:i + n], i + n
