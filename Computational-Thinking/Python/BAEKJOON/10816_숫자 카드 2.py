import sys
sys.stdin.readline().rstrip()
arr_N = sys.stdin.readline().split()
sys.stdin.readline().rstrip()
arr_M = sys.stdin.readline().split()
cnt = {}
for _ in arr_N:
    if _ in cnt:
        cnt[_] += 1
    else:
        cnt[_] = 1
for _ in arr_M:
    if _ in cnt:
        print(cnt[_], end = ' ')
    else:
        print(0, end = ' ')