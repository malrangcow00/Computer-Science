# 백트래킹 연습문제
# powerset 중 합이 N인 부분집합을 모두 출력하는 문제
def subset(i, s):
    # 기저조건
    if s > 10:
        return
    elif i == N and s != 10:
        return
    elif s == 10:
        print(*result)
        return

    # i 번째에 있는 요소를 사용o
    result.append(arr[i])
    subset(i + 1, s + arr[i])

    # i 번째에 있는 요소를 사용x
    result.pop()
    subset(i + 1, s)


arr = list(range(1, 11))
N = len(arr)
result = []  # 부분집합을 저장할 리스트
subset(0, 0)