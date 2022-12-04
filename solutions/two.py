'''
Appreciative of your help yesterday, one Elf gives you an encrypted strategy
guide (your puzzle input) that they say will be sure to help you win.

"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response:
X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious,
so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of
your scores for each round.

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score
you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y).
This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).

In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
This ends in a loss for you with a score of 1 (1 + 0).

The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
'''

# score = choice of rock, paper, scissors plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
WON_PTS = 6
DRAW_PTS = 3
LOST_PTS = 0

ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'


def solveB(input):
    input = input.split("\n")

    sum = 0
    for line in input:
        pair = line.split(' ')
        opp, outcome = pair[0], pair[1]
        sum += resolve_game_v2(opp, outcome)

    return sum


def solveA(input):
    input = input.split("\n")

    sum = 0
    for line in input:
        pair = line.split(' ')
        opp, you = pair[0], pair[1]
        sum += resolve_game(you, opp)

    return sum


# first column: A for Rock, B for Paper, and C for Scissors
# second column: X for Rock, Y for Paper, and Z for Scissors.
MAPPING_V2 = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': LOST_PTS,
    'Y': DRAW_PTS,
    'Z': WON_PTS
}

MAPPING = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}

# mapping of opponent choice => wanted outcome => choice you should make
# ex: opp chooses ROCK and you want to win, player_choice = STRATEGY_MAPPING[ROCK][WON_PTS]
STRATEGY_MAPPING = {
    ROCK: {
        LOST_PTS: SCISSORS,
        WON_PTS: PAPER
    },
    PAPER: {
        LOST_PTS: ROCK,
        WON_PTS: SCISSORS
    },
    SCISSORS: {
        LOST_PTS: PAPER,
        WON_PTS: ROCK
    }
}

POINTS = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}


def resolve_game_v2(opp, outcome):
    # convert to common language
    opp_play, outcome_pts = MAPPING_V2[opp], MAPPING_V2[outcome]

    # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    current_points = outcome_pts
    if outcome_pts == DRAW_PTS:
        current_points += POINTS[opp_play]
    else:
        my_play = STRATEGY_MAPPING[opp_play][outcome_pts]
        current_points += POINTS[my_play]

    return current_points


def resolve_game(a, b):
    # convert to common language
    a_play, b_play = MAPPING[a], MAPPING[b]

    # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    current_points = POINTS[a_play]

    # plus the score for the outcome of the round
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).
    if a_play == b_play:
        current_points += DRAW_PTS
    elif a_play == ROCK:
        if b_play == PAPER:
            current_points += LOST_PTS
        elif b_play == SCISSORS:
            current_points += WON_PTS
    elif a_play == PAPER:
        if b_play == ROCK:
            current_points += WON_PTS
        elif b_play == SCISSORS:
            current_points += LOST_PTS
    elif a_play == SCISSORS:
        if b_play == ROCK:
            current_points += LOST_PTS
        elif b_play == PAPER:
            current_points += WON_PTS
    else:
        print('well this is awkward: ' + a_play)

    return current_points
