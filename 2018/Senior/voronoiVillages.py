"""Canadian Computing Competition: 2018 Stage 1, Senior #1
In the country of Voronoi, there are N villages, located at distinct points on a straight road. Each of these villages will be represented by an integer position along this road.

Each village defines its neighbourhood as all points along the road which are closer to it than to any other village. A point which is equally close to two distinct villages A and B is in the neighbourhood of A and also in the neighbourhood of B.

Each neighbourhood has a size which is the difference between the minimum (leftmost) point in its neighbourhood and the maximum (rightmost) point in its neighbourhood.

The neighbourhoods of the leftmost and rightmost villages are defined to be of infinite size, while all other neighbourhoods are finite in size.

Determine the smallest size of any of the neighbourhoods (with exactly 1 digit after the decimal point).

[Input Specification]
The first line will contain the number N (3 ≤ N ≤ 100), the number of villages. On the next N lines there will be one integer per line, where the ith line contains the integer Vi , the position of the ith village (−1000000000≤Vi≤1000000000). All villages are at distinct positions.

[Output Specification]
Output the smallest neighbourhood size with exactly one digit after the decimal point."""


# Sort, get midpoint of each adjacent village, find minimum.

villages = sorted(int(input()) for index in range(int(input())))
smallest = float("Inf")
for index in range(2, len(villages)):
    smallest = min(smallest, (villages[index] - villages[index - 2]) / 2)
print("%.1f" % smallest)
