"""Canadian Computing Competition: 2018 Stage 1, Junior #5
There is a genre of fiction called choose your own adventure books. These books allow the reader to make choices for the characters which alters the outcome of the story.

For example, after reading the first page of a book, the reader may be asked a choice, such as "Do you pick up the rock?" If the reader answers "yes", they are directed to continue reading on page 47, and if they choose "no", they are directed to continue reading on page 18. On each of those pages, they have further choices, and so on, throughout the book. Some pages do not have any choices, and thus these are the "ending" pages of that version of the story. There may be many such ending pages in the book, some of which are good (e.g., the hero finds treasure) and others which are not (e.g., the hero finds a leftover sandwich from 2001).

You are the editor of one of these books, and you must examine two features of the choose your own adventure book:

ensure that every page can be reached – otherwise, there is no reason to pay to print a page which no one can ever read;
find the shortest path, so that readers will know what the shortest amount of time they need to finish one version of the story.
Given a description of the book, examine these two features.

Input Specification
The first line of input contains N (1≤N≤10000), the number of pages in the book. Each of the next N lines contain an integer Mi (1≤i≤N;0≤Mi≤N), which is the number of different options from page i, followed by Mi space-separated integers in the range from 1 to N, corresponding to each of the pages to go to next from page i. It will also be the case M1+M2+⋯+MN is at most 10000.

If Mi=0, then page i is an ending page (i.e., there are no choices from that page). There will be at least one ending page in the book.

Note that you always begin the book on page 1.

For 4 of the available 15 marks, N≤100, Mi≤10 for 1≤i≤N.

For an additional 3 of the available 15 marks, the book is guaranteed to have no cycles.

For an additional 4 of the available 15 marks, N≤1000, Mi≤25 for 1≤i≤N.

Output Specification
The output will be two lines. The first line will contain Y if all pages are reachable, and N otherwise.

The last line will contain a non-negative integer K, which is the shortest path a reader can take while reading this book. There will always be a finite shortest path."""


### Approach: Run two BFS, first to check if all nodes can be reached, second to find the shortest path.


vertices = int(input())
adjList = []
for i in range(vertices):
  adjList.append([int(node) - 1 for node in input().split()][1:] or [])
queue = {0}
visited = set()
### First BFS
while queue:
  visited |= queue
  queue = {node for vertice in queue for node in adjList[vertice] if node not in visited}
print("NY"[len(visited) == vertices])

### Second BFS
queue = [[0]]
visited = set()
while queue:
  path = queue.pop(0)
  node = path[-1]
  if len(adjList[node]) == 0:
    break
  for vertice in adjList[node]:
    if vertice in visited:
      pass
    visited.add(vertice)
    queue.append(path + [vertice])
print(len(path))
