def solve_a(problem_input):
    state, commands = process_input(problem_input)
    for command in commands:
        state = apply(state, command)

    return get_topmost_crates(state)


def solve_b(problem_input):
    state, commands = process_input(problem_input)
    for command in commands:
        state = apply_b(state, command)

    return get_topmost_crates(state)

def get_topmost_crates(state):
    top = ""
    for stack in state:
        if len(stack) > 0:
            top += state[stack][-1]

    return top


def apply_b(state, command):
    num_items, from_stack, to_stack = parse_command(command)
    state = move_b(state, from_stack, to_stack, num_items)
    return state


def move_b(state, from_stack, to_stack, num_items):
    moving = state[from_stack][-1 * (int(num_items))::]
    staying = state[from_stack][0:-1 * int(num_items)]

    state[from_stack] = staying
    state[to_stack] += moving
    return state

def apply(state, command):
    times, from_stack, to_stack = parse_command(command)
    for i in range(int(times)):
        state = move(state, from_stack, to_stack)
    return state


def move(state, from_stack, to_stack):
    top = state[from_stack].pop()
    state[to_stack].append(top)
    return state

def parse_command(command):
    pieces = command.split(" ")
    times = pieces[1]
    from_stack = pieces[3]
    to_stack = pieces[5]

    return times, from_stack, to_stack



def process_input(problem_input):
    # break the input into discrete blocks for processing
    # the stack id line is a good break up point for the file
    # because the stacks and commands sandwich it
    stack_id_index = get_stack_id_index(problem_input)

    stacks_block = problem_input[0:stack_id_index]
    stack_id_block = problem_input[stack_id_index]
    initial_state = build_initial_state(stack_id_block, stacks_block)

    # +2 because there's an extra line added
    command_block = problem_input[stack_id_index + 2:]

    return initial_state, command_block


def get_stack_id_index(problem_input):
    # find start of numbered stacks,
    # index represents index of where the stack labels are
    index = 0
    for line in problem_input:
        if '1' in line:
            break
        else:
            index += 1
    return index

# build initial state
# {'1': [], '2': [], '3': []}
def build_initial_state(stack_id_block, stacks_block):
    stack_ids = stack_id_block.strip().split("   ")
    state = {stack_id: [] for stack_id in stack_ids}
    stacks_block.reverse()
    for stack_id in state:

        horizontal_index = stack_id_block.index(stack_id)
        for line in stacks_block:
            try:
                item = line[horizontal_index]
                if item != " ":
                    state[stack_id].append(item)
            except IndexError:
                # no need to process line
                # if there's no more values to process
                break

    return state

