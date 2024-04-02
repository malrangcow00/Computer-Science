def kmp(t, p):
    N = len(t)
    M = len(p)

    # next 배열을 만드는 전처리... (prepressing)
    j = 0  # 일치한 갯수 == 비교할 패턴 인덱스
    lps = [0] * (M + 1)
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j

    # 검색
    i = 0  # 비교할 텍스트(t) 인덱스
    j = 0  # 비교할 패턴(p) 인덱스
    while i < N and j <= M:
        if p[j] == - 1 or t[i] == p[j]:  # 첫글자가 불일치... 일치 했을 때
            i += 1
            j += 1
        else:  # 일치 하지 않았을 때
            j = lps[j]
        if j == M:  # 패턴을 찾은 경우
            print(i - M, end=" ")  # 패턴이 매칭된 t기준의 시작점
            j = lps[j]

    print()
    return


t = 'abcdabcdabcefzzzzzzzzzz'
p = 'abcdabcef'
kmp(t, p)