from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

input()
C = list(map(int, input().split()))

deq = deque()
for _ in range(N):
    if A[_] == 0:
        deq.appendleft(B[_])
for _ in C:
    deq.append(_)
    print(deq.popleft(), end=' ')