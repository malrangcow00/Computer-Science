arr = [1, 2, 3, 4, 5]

# 재귀호출.. 해보자...
# 순열, 4개의 값을 뽑아내는 경우를 모두 출력해봐라...
result = []
# 체크리스트... True 값이 넣어져있으면 이미 사용한 요소...
checked = [False for _ in range(len(arr))]

cnt = 0


def generate_permutations(arr, depth):
    global cnt
    # 기저 조건
    if depth == 4:
        cnt += 1
        # result의 값을 출력
        print(result)
        return

    # arr 를 순회하면서 하나의 값을 뽑아낸다.
    for idx in range(len(arr)):
        # 해당 번호를 뽑게 되면, 다음에 뽑지 못하도록 체크를 해줘야함!
        if checked[idx]:
            continue
        # 사용
        checked[idx] = True
        result.append(arr[idx])
        generate_permutations(arr, depth + 1)  # 재귀호출
        # 복구
        checked[idx] = False
        result.pop()


# generate_permutations(arr, 0)
# print(cnt)


def generate_combination(arr, depth, current):
    global cnt
    # 기저 조건
    if depth == 4:
        cnt += 1
        # result의 값을 출력
        print(result)
        return

    # arr 를 순회하면서 하나의 값을 뽑아낸다.
    for idx in range(current, len(arr)):
        # 해당 번호를 뽑게 되면, 다음에 뽑지 못하도록 체크를 해줘야함!
        if checked[idx]:
            continue
        # 사용
        checked[idx] = True
        result.append(arr[idx])
        generate_combination(arr, depth + 1, idx + 1)  # 재귀호출
        # 복구
        checked[idx] = False
        result.pop()


generate_combination(arr, 0, 0)
print(cnt)