P = [1, 2, 3]

# 재귀적으로 요소 값을 교환을 하면서
# 만들 수 있는 순서를 만들어본다.
# i : 깊이 (재귀를 얼마나 호출했는가)
# N : 순열을 만들 리스트의 크기
N = len(P)

def f(i, N):
    # 기저 조건
    if i == N: # 순열 완성
        print(P)
        return
    for j in range(i, N):
        # 교환 (결정)
        P[i], P[j] = P[j], P[i]
        f(i + 1, N)
        # 복구
        P[i], P[j] = P[j], P[i]

f(0, N)
