T = int(input())

arr = [[0]*100 for i in range(100)]

for tc in range(T):
    x1, y1 = map(int, input().split())
    x2, y2 = x1 + 9, y1 + 9
    for y in range(100):
        if y2 >= y >= y1:
            for x in range(100):
                if x2 >= x >= x1:
                    arr[y][x] = 1

total = 0

for i in range(100):
    total += sum(arr[i])

print(total)
