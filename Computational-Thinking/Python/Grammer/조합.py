# 조합
# nCr : n개에서 r개를 고르는 조합. s 고를 수 있는 시작 인덱스
def nCr(n, r, s):
    # 기저조건 (r개를 모두 뽑았을 때)
    if r == 0:
        print(*reversed(comb))
        return

    # 유도조건
    for i in range(s, n - r + 1):
        comb[r - 1] = A[i]
        nCr(n, r - 1, i + 1)


# 10개 의 요소
n = 10

# 3개를 뽑겠다
r = 3

# 조합 3개를 뽑은 결과값을 임시 저장 리스트...
comb = [0] * r

# 10개의 요소를 가지고 있는 배열...
A = [i for i in range(1, n + 1)]
nCr(n, r, 0)