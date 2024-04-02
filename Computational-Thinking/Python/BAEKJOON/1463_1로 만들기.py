import sys
input = sys.stdin.readline

N = int(input())
mn = float('inf')
tmp = 0
def recur(N):
    global mn, tmp
    if N == 1:
       mn = min(mn, tmp)
       return
    else:
        tmp += 1
        recur(N-1)
        tmp -= 1
        if N % 3 == 0:
            tmp += 1
            recur(N//3)
            tmp -= 1
        if N % 2 == 0:
            tmp += 1
            recur(N//2)
            tmp -= 1
recur(N)
print(mn)