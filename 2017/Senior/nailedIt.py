
# CCC Senior 3 / Junior 5

"""Tudor is a contestant in the Canadian Carpentry Challenge (CCC). To win the CCC, Tudor must demonstrate his skill at nailing wood together to make the longest fence possible using boards. To accomplish this goal, he has N pieces of wood. The ith piece of wood has integer length Li.

A board is made up of exactly two pieces of wood. The length of a board made of wood with lengths Li and Lj is Li+Lj. A fence consists of boards that are the same length. The length of the fence is the number of boards used to make it, and the height of the fence is the length of each board in the fence. In the example fence below, the length of the fence is 4; the height of the fence is 50; and, the length of each piece of wood is shown:


Tudor would like to make the longest fence possible. Please help him determine the maximum length of any fence he could make, and the number of different heights a fence of that maximum length could have.

[Input Specification]
The first line will contain the integer N (2 ≤ N ≤ 1000000).
The second line will contain N space-separated integers L1,L2,…,LN (1 ≤ Li ≤ 2000).

For 5 of the 15 available marks, N≤100.
For an additional 4 of the 15 available marks, N ≤ 1000.
For an additional 3 of the 15 available marks, N ≤ 100000.

[Output Specification]
Output two integers on a single line separated by a single space: the length of the longest fence and the number of different heights a longest fence could have."""


from sys import stdin

def nail(boards):
    heights = {}
    get = heights.get
    for boardA in range(1, 2001):
        if boardA not in boards:
            continue
        heights[boardA * 2] = get(boardA * 2, 0) + (boards[boardA] >> 1)
        for boardB in range(boardA + 1, 2001):
            if boardB not in boards:
                continue
            height = boardA + boardB
            heights[height] = get(height, 0) + min(boards[boardA], boards[boardB])
    maximum = -1
    counter = 0
    for i in heights:
        i = heights[i]
        if i > maximum:
            maximum = i
            counter = 0
        if i == maximum:
            counter += 1
    print(maximum, counter)
    return None

stdin.readline()
freq = {}
for i in map(int, stdin.readline().split()):
    freq[i] = freq.get(i, 0) + 1
nail(freq)
