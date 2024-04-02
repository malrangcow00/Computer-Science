from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
que = deque()
for _ in range(N):
    cmd = input().rstrip()
    if cmd[:2] == 'pu':
        que.append(cmd[5:])
    elif cmd[:2] == 'po':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd[0] == 's':
        print(len(que))
    elif cmd[0] == 'e':
        if que:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'f':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)