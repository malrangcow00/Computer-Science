import sys
input = sys.stdin.readline

S = input().rstrip()
arr = [[0]*26]
arr[0][ord(S[0]) - 97] = 1
for i in range(1, len(S)):
    arr.append(arr[-1][:])
    arr[i][ord(S[i]) - 97] += 1

for _ in range(int(input())):
    alpha, l, r = list(input().split())
    l, r = map(int, [l, r])
    if l == 0:
        print(arr[r][ord(alpha) - 97])
    else:
        print(arr[r][ord(alpha) - 97] - arr[l - 1][ord(alpha) - 97])