N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([y, x])

arr.sort()
# arr = sorted(arr)

for _ in arr:
    print(_[1], _[0])

    
# N = int(SWEA.input())

# arr = []
# for _ in range(N):
#     x, y = map(int, SWEA.input().split())
#     arr.append([x, y])

# arr.sort(key = lambda x: (x[1], x[0]))

# for _ in arr:
#     print(_[0], _[1])