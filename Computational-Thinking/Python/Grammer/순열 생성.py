def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N): # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i] # 주석처리 한 경우와 비교해보기

A = [1, 2, 3]
f(0, len(A))
