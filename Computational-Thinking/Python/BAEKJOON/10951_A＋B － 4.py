import sys

lines = sys.stdin.readlines()
for i in lines:
    A, B = map(int, i.split())
    print(A + B)
