import sys

N = int(sys.stdin.readline())
history = {}
for _ in range(N):
    p = sys.stdin.readline().split()[0]
    if p not in history.keys():
        history[p] = 0
    history[p] += 1
lst = []
for key, value in history.items():
    if value % 2 == 1:
        lst.append(key)
lst.sort(reverse=True)
for _ in lst:
    print(_)