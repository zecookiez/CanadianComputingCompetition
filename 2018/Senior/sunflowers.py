"""Barbara plants N different sunflowers, each with a unique height, ordered from smallest to largest, and records their heights for N consecutive days. Each day, all of her flowers grow taller than they were the day before.

She records each of these measurements in a table, with one row for each plant, with the first row recording the shortest sunflower's growth and the last row recording the tallest sunflower's growth.

The leftmost column is the first measurement for each sunflower, and the rightmost column is the last measurement for each sunflower.

If a sunflower was smaller than another when initially planted, it remains smaller for every measurement.

Unfortunately, her children may have altered her measurements by rotating her table by a multiple of 90 degrees.

Your job is to help Barbara determine her original data.

[Input Specification]
The first line of input contains the number N (2≤N≤100). The next N lines each contain N positive integers, each of which is at most 109 . It is guaranteed that the input grid represents a rotated version of Barbara's grid.

[Output Specification]
Output Barbara's original data, consisting of N lines, each of which contain N positive integers."""


grid = [[*map(int, input().split())] for i in range(int(input()))]

lowest = min(map(min, grid))

while lowest != grid[0][0]:
    grid = [*zip(*grid[::-1])]

for i in grid:
    print(" ".join(map(str, i)))
