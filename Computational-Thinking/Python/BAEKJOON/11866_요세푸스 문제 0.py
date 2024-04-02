from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
que = deque(range(1, N+1))
print('<', end='')
while len(que) > 1:
    for _ in range(K-1):
        que.append(que.popleft())
    print(que.popleft(), end=', ')
print(que.popleft(), end='')
print('>')