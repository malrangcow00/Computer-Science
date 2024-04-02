import sys
input = sys.stdin.readline

def fibonacci(N):
    if N < 2:
        return N
    else:
        return fibonacci(N-1)+fibonacci(N-2)

print(fibonacci(int(input())))