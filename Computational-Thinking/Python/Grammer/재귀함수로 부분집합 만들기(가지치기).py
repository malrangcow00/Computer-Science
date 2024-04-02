# 재귀함수로 부분집합 만들기

# bits : 해당 인덱스의 요소를 사용할지의 유무 (1:o, 0:x)
# depth : 내가 얼마나 함수를 재귀호출했는지에 대한 카운트값..
# current : 현재까지 부분 집합 요소들의 중간합
def recur(bits, depth, current):
    if current > 10:  # 가지치기
        return

    # 기저조건
    if depth == N:
        if current == 10:
            # 총합이 10이라면...
            # 부분집합을 출력하는 코드
            for i in range(N):
                if bits[i] == 1:
                    print(arr[i], end=' ')
            print()
        return

    for i in range(2):  # 0, 1
        bits[depth] = i
        # 자기 자신을 호출
        if bits[depth] == 1:
            recur(bits, depth + 1, current + arr[i])
        else:  # 0
            recur(bits, depth + 1, current)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
recur([0] * N, 0, 0)