# s: i-1 원소까지 고려한 합
# t : 찾으려는 합
def f(i, N, s):
    if i == N:
        if s == 10:
            print(bit, end = '')
            print(f' : {s}')
            return

    else:
        bit[i] = 1
        f(i+1, N, s+A[i])
        bit[i] = 0
        f(i+1, N, s)
        return

A = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
bit = [0] * len(A)
N = len(A)
f(0, N, 0)
