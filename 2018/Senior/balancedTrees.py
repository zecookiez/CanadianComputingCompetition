"""Trees have many fascinating properties. While this is primarily true for trees in nature, the concept of trees in math and computer science is also interesting. A particular kind of tree, a perfectly balanced tree, is defined as follows.

Every perfectly balanced tree has a positive integer weight. A perfectly balanced tree of weight 1 always consists of a single node. Otherwise, if the weight of a perfectly balanced tree is w and w≥2, then the tree consists of a root node with branches to k subtrees, such that 2≤k≤w. In this case, all k subtrees must be completely identical, and be perfectly balanced themselves.

In particular, all k subtrees must have the same weight. This common weight must be the maximum integer value such that the sum of the weights of all k subtrees does not exceed w, the weight of the overall tree. For example, if a perfectly balanced tree of weight 8 has 3 subtrees, then each subtree would have weight 2, since 2+2+2=6≤8.

Given N, find the number of perfectly balanced trees with weight N.

[Input Specification]
The input will be a single line containing the integer N (1≤N≤10^9).

For 5 of the 15 marks available, N≤1000.

For an additional 2 of the 15 marks available, N≤50000.

For an additional 2 of the 15 marks available, N≤106.

[Output Specification]
Output a single integer, the number of perfectly balanced trees with weight N."""

# Technically only passed with PyPy on dmoj, hopefully this passes in the real CCC but I'm too scared to try it :P

# Recurrence formula:	a(n) = a([ n/2 ]) + a([ n/3 ]) + . . . + a([ n/n ])
# See https://oeis.org/A022825 for more info (there isn't a lot)


# Method: Recursion + memoization
# Instead of doing n/2, n/3 ... n/n, I used a formula to count the frequency of each number
from sys import stdin
N = int(stdin.readline())
memo = {}
def f(n):
    if n == 1: #Base case, one "tree" always has one node
        return 1
    if n not in memo:
        total = n - (n >> 1)
        kth = 2
        while True:
            partition = n // kth
            if partition ** 2 > n:
                total += f(kth) * (partition - n // (kth + 1)) + f(partition)
            elif kth == partition:
                total += f(kth) * (partition - n // (kth + 1))
            else:
                break
            kth += 1
        memo[n] = total
    return memo[n]
print(f(N))
