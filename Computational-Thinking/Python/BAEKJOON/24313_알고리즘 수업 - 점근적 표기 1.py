a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

def f(n):
    global a1, a0
    return a1*n + a0

def g(n):
    return n

if f(n0) <= c*g(n0) and a1 <= c:
    print(1)
else:
    print(0)