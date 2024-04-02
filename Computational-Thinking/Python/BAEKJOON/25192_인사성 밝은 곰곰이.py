import sys
input = sys.stdin.readline

N = int(input())
entrance = []
input()
cnt = 0
for _ in range(N-1):
    name = input().rstrip()
    if name == 'ENTER':
        cnt += len(set(entrance))
        entrance.clear()
    else:
        entrance.append(name)
cnt += len(set(entrance))
print(cnt)