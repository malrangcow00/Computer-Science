N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort()
# arr = sorted(arr)

for _ in arr:
    print(_[0], _[1])