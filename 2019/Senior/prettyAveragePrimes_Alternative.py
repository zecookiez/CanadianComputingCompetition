from sys import stdin

input = stdin.readline

MAXN = 2000002 # Make sure the limit is greater than 1 million because the pairs could be greater than N itself.
sieve = [1]*MAXN
sieve[0] = 0 # Cross out
sieve[1] = 0
primes = [2]

for i in xrange(2, MAXN, 2):
    sieve[i] = 0 # Cross out even numbers

# Classic Sieve of Eratosthenes to precomputer all the primes

for i in xrange(3, MAXN, 2):
    if sieve[i]:
        primes.append(i)
        for j in xrange(i * i, MAXN, i + i):
            sieve[j] = 0

for i in xrange(int(input())):
    n = int(input()) * 2
    # If you rearrange the equation,
    #   2N = A + B
    #   We fix point A, then identify B as 2N - A
    for a in primes:
        if sieve[n - a]:
            print a, n - a
            break
