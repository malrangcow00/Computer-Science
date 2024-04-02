import sys
sys.stdin = open('input/1926.txt', 'r')

N = int(input())

lst = []
for _ in range(1, N+1):
    lst.append(str(_))

for _ in range(N):
    for target in ['3', '6', '9']:
        lst[_] = lst[_].replace(target, '-')
    if len(lst[_]) > 1 and '-' in lst[_]:
        cnt = 0
        for i in lst[_]:
            if i != '-':
                cnt += 1
        lst[_] = '-' * (len(lst[_]) - cnt)
print(*lst)