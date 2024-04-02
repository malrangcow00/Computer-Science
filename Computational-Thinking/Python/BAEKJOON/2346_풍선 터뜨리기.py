from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque(map(int, input().split()))
deq = deque([value, index] for index, value in enumerate(deq, 1))
pan = deq.popleft()
print(1, end=' ')
while deq:
    if pan[0] >= 0:
        for _ in range(pan[0]-1):
             deq.append(deq.popleft())
        pan = deq.popleft()
        print(pan[1], end=' ')
    else:
        for _ in range(abs(pan[0])-1):
            deq.appendleft(deq.pop())
        pan = deq.pop()
        print(pan[1], end=' ')