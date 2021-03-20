rows = [0] * int(input())
cols = [0] * int(input())

# My approach:
#   A cell can be uniquely identified by the x and y coordinate
#   We can keep track of those instead
#   You can keep track of the parity to determine Gold/Black

for _ in range(int(input())):
    t, id = input().split()
    if t == "R": rows[int(id) - 1] ^= 1
    else: cols[int(id) - 1] ^= 1

# A little bit of inclusion-exclusion
# O(N * M) works here too

A = rows.count(1)
B = cols.count(1)
print(A * len(cols) + B * len(rows) - 2 * A * B)
