# 재귀함수로 부분집합 만들기

# bits : 해당 인덱스의 요소를 사용할지의 유무 (1:o, 0:x)
# depth : 내가 얼마나 함수를 재귀호출했는지에 대한 카운트값..
def recur(bits, depth):
    # 기저조건
    if depth == N:
        tmp = []
        for i in range(N):
            if bits[i] == 1:
                tmp.append(arr[i])
        if sum(tmp) == 10:
            print(*tmp)
        return

    for i in range(2):  # 0, 1
        bits[depth] = i
        # 자기 자신을 호출
        recur(bits, depth + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
recur([0] * N, 0)