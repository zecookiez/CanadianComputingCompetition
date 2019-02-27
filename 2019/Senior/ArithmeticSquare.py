from random import randint
from sys import stdin
input = stdin.readline

# Outline of approach because this problem tripped lots of people (including me) during the contest:
#
# 1 - While the grid is not completely filled in:
#     1a - Fill in anything that can be deduced (ex: there is only 1 X in a row, we can deduce that value)
#     1b - Find all leftover X spots
#     1c - Generate a random value to put in that square
#              The reason this works is because the only real cases where there are leftover spots is when there are very few numbers actually filled in.
#              Therefore there can be many different solutions to that grid.
#              In fact, there are so many that we can just put a random value in there and try another one if it fails.
#
# This method is pretty short, takes less than 40 lines to write (compared to my original 200 lines solution)


# Function that will fill in any number that can be deduced
def fill(grid):
    for _ in xrange(9):
        for side in xrange(2):
            for pos, (i, j, k) in enumerate(grid):
                if j == "X":
                    if i != "X" != k:
                        j = i + k >> 1
                elif k == "X":
                    if i != "X" != j:
                        k = j + j - i
                elif i == "X":
                    if j != "X" != k:
                        i = j + j - k
                grid[pos] = i, j, k
            grid = map(list, zip(*grid))
            
    # Make sure that our grid is still valid
    if any(i + k != j + j for table in (grid, zip(*grid)) for i, j, k in table if X not in (i, j, k)):
        return 0
        
    return grid

def helper(state): 

    state = fill(state)
    
    if state == 0: # Invalid grid.
        return 0
    
    if all(i != "X" for row in state for i in row):
        return state
        
    for row in xrange(3):
        if "X" in state[row]:
            col = state[row].index("X")
            for _ in xrange(10):
                state[row][col] = randint(-1000000, 1000000) # Fill a random value
                value = helper(state[:])
                if value:
                    return value
            state[row][col] = X
        
X = "X" # Used for eval. This is just a nice trick to read the input
for i, j, k in helper([map(eval, input().split()) for i in xrange(3)]):
    print i, j, k
