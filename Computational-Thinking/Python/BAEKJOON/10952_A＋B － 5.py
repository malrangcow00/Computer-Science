import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    sum = A + B
    if sum != 0:
        print(sum)
    else:
        break
