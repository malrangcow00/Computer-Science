import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deq = deque()
for _ in range(N):
    tmp = input().split()
    if tmp[0] == 'size':
        print(len(deq))
    elif tmp[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif tmp[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif tmp[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
    elif tmp[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif tmp[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif tmp[0] == 'push_front':
        deq.appendleft(tmp[1])
    elif tmp[0] == 'push_back':
        deq.append(tmp[1])