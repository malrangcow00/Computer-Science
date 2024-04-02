mx = 0
mx_y = 0
mx_x = 0

for y in range(1, 10):
    arr = list(map(int, input().split()))
    for x, value in enumerate(arr, start = 1):
        if mx <= value:
            mx = value
            mx_x = x
            mx_y = y
print(mx)
print(mx_y, mx_x)