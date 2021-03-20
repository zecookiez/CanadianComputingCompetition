N = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

# Split into trapezoids

area = 0
for i in range(1, N + 1):
    area += (arr[i] + arr[i - 1]) * brr[i - 1] / 2.0

print(area)