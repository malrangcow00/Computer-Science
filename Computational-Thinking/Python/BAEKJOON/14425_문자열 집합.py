import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline())
cnt = 0
for _ in range(M):
    if sys.stdin.readline() in arr:
        cnt += 1
print(cnt)