###See other file for the problem description



#On DMOJ, this passed the tests in py3 in 1.35 seconds and took 10.3MB of memory which was a pretty decent amount lower than the other top python3 solutions.

import sys
from collections import deque

vertices = int(sys.stdin.readline()) #input
adjList = [[int(node) - 1 for node in sys.stdin.readline().split()[1:]] for i in range(vertices)] #Build graph
queue = deque([[0]]) #Initialize queue
visited = 1 #Use bitmask to track visited vertices, this will help save some memory and speed (Faster than set lookup)
lowest = -1 #Shortest path
while queue:
  path = queue.popleft()
  node = path[-1]
  if not adjList[node] and lowest < 0:
    lowest = len(path)
  if lowest > -1 and visited + 1 == 1 << vertices:
    break
  for vertice in adjList[node]:
    if visited >> vertice & 1: #Grab kth bit of bitmask, check if it visited or not
      continue
    visited |= 1 << vertice #Mark it
    if lowest < 0:
      queue.append(path + [vertice]) #Memory save, no need to keep path if you already found the shortest path
    else:
      queue.append([vertice])
print("NY"[visited + 1 == 1 << vertices]) # 1 + visited == 2 ** vertices, which means all the bits in the bitmask got marked
print(lowest)
