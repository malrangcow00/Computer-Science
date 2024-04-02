import sys

N, B = map(int, sys.stdin.readline().split())

lst = []

while N != 0:
    lst.append(N % B)
    N //= B

lst.reverse()

for i in lst:
    if i in range(10):
        print(i, end = '')
    else:
        print(chr(i+55), end = '')
print()