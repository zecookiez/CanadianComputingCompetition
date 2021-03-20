import heapq
from collections import deque

"""
My approach:
    An important observation I used is that the only optimal way to reach node N is by taking the subway first, then going to node N by foot
    The answer to each output is min(index + dist[i] for i in perm)
    Calculating dist[i] is O(N + M) by reversing the edges and doing BFS from node N
    You can maintain the best answer using a multiset (Used a priority queue with lazy deletion due to python's lack of multiset)
"""

# Input parsing
N, W, D = list(map(int, input().split()))

# Build adjacency list (But reverse the edge directions)
adj = [[] for i in range(N + 1)]
for _ in range(W):
    a, b = list(map(int, input().split()))
    adj[b].append(a)

subway = list(map(int, input().split()))

# Perform BFS from node N instead
dist = [N + 1] * (N + 1)
dist[N] = 0
queue = deque([N])
while queue:
    node = queue.popleft()
    for nxt in adj[node]:
        # Still unvisited?
        if dist[nxt] == N + 1:
            dist[nxt] = dist[node] + 1
            queue.append(nxt)

# Insert everything into the heap
ans = []
for i in range(N):
    heapq.heappush(ans, (i + dist[subway[i]], i, subway[i]))

output = []
for _ in range(D):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    subway[x], subway[y] = subway[y], subway[x]
    
    # Insert the newly updated elements into the heapq
    heapq.heappush(ans, (x + dist[subway[x]], x, subway[x]))
    heapq.heappush(ans, (y + dist[subway[y]], y, subway[y]))
    
    # Find the lowest time that is still available
    while True:
        # ans[0] returns the smallest time (thanks heapq)
        time, index, station = ans[0]
        # Is this still a valid station (did no swaps affect it)
        if subway[index] == station:
            output.append(time)
            break
        # If it is invalid, remove it
        heapq.heappop(ans)

print("\n".join(map(str, output)))