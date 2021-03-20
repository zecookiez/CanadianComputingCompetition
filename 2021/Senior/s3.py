N = int(input())
people = [list(map(int, input().split())) for i in range(N)]

def calc_time(x):
    tot_time = 0
    for pos, w, d in people:
        # Already in range?
        if abs(pos - x) <= d: 
            continue
        # Left side
        if pos < x:
            tot_time += ((x - d) - pos) * w
        # Right side
        else:
            tot_time += (pos - (x + d)) * w
    return tot_time

left = 0
right = 10**9

# Binary search on the slope
while left + 1 < right:
    mid = (left + right) // 2
    # Slope = change in Y value
    y1 = calc_time(mid)
    y2 = calc_time(mid + 1)
    if y1 >= y2: 
        left = mid  # Still decreasing
    else:
        right = mid  # Otherwise increasing

print(min(calc_time(left), calc_time(right)))
