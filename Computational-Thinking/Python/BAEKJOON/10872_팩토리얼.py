import sys
input = sys.stdin.readline

N = int(input())
result = 1
while 0 < N:
    result *= N
    N -= 1
print(result)