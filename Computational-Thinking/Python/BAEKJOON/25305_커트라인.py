N, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for _ in range(k-1):
    arr.pop()
print(arr.pop())