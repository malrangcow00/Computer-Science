import sys
input = sys.stdin.readline

def factorial(N, i):
    if N == 0:
        return i
    else:
        i *= N
        N -= 1
        return factorial(N, i)

print(factorial(int(input()), 1))