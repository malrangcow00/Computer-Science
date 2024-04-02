import sys
input = sys.stdin.readline

cnt = [0] * 10
for i in str(int(input()) * int(input()) * int(input())):
    cnt[int(i)] += 1
for i in cnt:
    print(i)