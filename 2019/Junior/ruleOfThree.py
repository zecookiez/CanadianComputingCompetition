# Main idea is to use recursion to go through each substitution
# To speed this up, we will NOT go through identical states (# of steps, state)

# I wrote senior this year so I cannot confirm this will pass, but running my own tests shows that it's capable of doing steps=15 :)

from sys import stdin
input = stdin.readline

t1, d1 = input().split()
t2, d2 = input().split()
t3, d3 = input().split()

steps, src, tgt = input().split()
steps = int(steps)

# Main function

memo = set()

def helper(cur, state, moves):
    
    # We have reached the amount of steps and we have reached the target
    
    if cur == 0 and state == tgt:
        return moves
    
    # We ran out of steps and it's still different
    
    if cur == 0:
        return False

    # The most important part. This will allow the solution to pass for steps=15

    # Main idea here is that we avoid computing the cases where different combinations will lead to the same state

    label = cur, state

    if label in memo:
        return False # Avoid it

    memo.add(label) # Don't go through this stage again
    
    # Go through each rule
    
    for rule, (a, b) in enumerate([(t1, d1), (t2, d2), (t3, d3)], 1):
        
        # Find all potential positions to use the rule
        
        l = len(a)
        pos = -1

        while 1:

            pos = state.find(a, pos + 1)

            if pos == -1: # If it doesn't find anything
                break
                
            # Create the new replaced sequence

            new_state = state[:pos] + b + state[pos + l:]
            output = helper(cur - 1, new_state[:], moves + [(rule, pos, new_state)])

            if output: # We found it!
                return output
    
    return False
    
value = helper(steps, src, [])

if not value:
    print("IMPOSSIBLE") # just in case, in the real problem this will never happen
else:
    for i, j, k in value:
        print(i, j + 1, k)
