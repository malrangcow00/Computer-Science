import sys

T = int(input())

for i in range(T):
    num = sys.stdin.readline().rstrip()
    A, B = map(int, num.split())
    print(A + B)
