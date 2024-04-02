import sys
input = sys.stdin.readline
N = int(input())
inquality = input().split()
mxnums = list(range(9-N, 10))
mnnums = list(range(N+1)[::-1])
mx = []
mn = []
bigger = False
cnt = 2
for i in inquality:
    if i == '>' and bigger == False:
        for j in range(1, cnt)[::-1]:
            mx.append(mxnums.pop(-j))
        bigger = True
        cnt = 3
    elif i == '>':
        mx.append(mxnums.pop())
        cnt += 1
    elif i == '<' and bigger == True:
        for j in range(1, cnt)[::-1]:
            mn.append(mnnums.pop(-j))
        bigger = False
        cnt = 3
    elif i == '<':
        mn.append(mnnums.pop())
        cnt += 1
for j in mxnums:
    mx.append(j)
for j in mnnums:
    mn.append(j)
print(''.join(map(str, mx)))
print(''.join(map(str, mn)))