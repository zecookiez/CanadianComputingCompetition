from sys import stdin
from collections import defaultdict
from math import gcd
input = stdin.readline
GI = lambda: int(input())
gi = lambda: list(map(int, input().split()))

# My approach:
#   If a subarray has GCD of x, then try setting all [L, R] as x 
#   For every index, it should be LCM of all intervals present
#   I did this using line sweep by index, keeping track of the GCDs using a dictionary
#   Since x <= 16, we can use O(16) LCM calculation
#   Finally, the array is impossible if GCD(L..R) != X, which I used a sparse table to obtain the GCD 


N, M = gi()
arr = [[] for i in range(N + 1)]
queries = []
for i in range(M):
    l, r, g = gi()
    l -= 1
    r -= 1
    arr[l].append((0, g))
    arr[r + 1].append((1, g))
    queries.append((l, r, g))

lcm = lambda a, b: a * b // gcd(a, b)

current = defaultdict(int)
output = []
for i in range(N):
    for j, k in arr[i]:
        if j == 0:
            current[k] += 1
        else:
            current[k] -= 1
            if current[k] == 0:
                current.pop(k)
    out = 1
    for i in current:
        out = lcm(out, i)
    output.append(out)

sparse = [list(output)]
i = 1
n = len(output)
while i * 2 <= n:
    prev = sparse[-1]
    sparse.append([gcd(prev[j], prev[j + i]) for j in range(n - i * 2 + 1)])
    i *= 2

def query(L, R):
    d = (R - L).bit_length() - 1
    return gcd(sparse[d][L], sparse[d][R - (1 << d)])

for l, r, g in queries:
    if query(l, r + 1) != g:
        print("Impossible")
        break 
else:
    print(" ".join(map(str, output)))