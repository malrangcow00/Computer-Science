import sys
input = sys.stdin.readline

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 메모이제이션, 병합정렬 최댓값을 기록
memo = {
    1 : 0, # 정렬할 필요 없음
    2 : 2, # [2, 1] -> [1, _ ] -> [1, 2]
    3 : 5  # memo[2] + memo[1] + 3
}

# 병합정렬 중 저장횟수 구하기
def mergeSortCount(N, msMemo):
    if N in msMemo:
        return msMemo[N]
    nthMemo = mergeSortCount((N+1)//2, msMemo) + mergeSortCount(N-(N+1)//2, msMemo) + N
    memo[N] = nthMemo
    return nthMemo

# 만약 배열 크기에 따른 저장횟수가 입력받은 저장횟수보다 작으면 바로 -1 출력 
if mergeSortCount(N, memo)<K:
    print(-1)
    quit()

# 병합정렬mergeSort
def mergeSort(array):
    if len(array)<= 1:
        return array

    # 분할 정복 위한 나누기
    mid = (len(array)+1)//2

    left_array = mergeSort(array[:mid])
    right_array = mergeSort(array[mid:])

    # 서로 다른 두 배열을 순서대로 merge하기 
    return merge(left_array, right_array)

#전역 변수로 숫자 정렬할 때마다 카운트하는 변수 선언
global hmSavingNum
hmSavingNum= 0

# 병합정렬merge
def merge(array1, array2):
    result = []

    # 병합하면서 새롭게 넣은 배열의 경우 다음 인덱스로 넘기기 위해 설정
    index1 = 0
    index2 = 0

    global hmSavingNum

    # 둘 다 새로운 배열에 옮겨담지 못했을 때
    while index1<len(array1) and index2<len(array2):
        if array1[index1] < array2[index2]:
            result.append(array1[index1])
            index1 += 1
        else:
            result.append(array2[index2])
            index2 += 1
        # 위의 두 조건문에 반복되어 밖으로 뺐다.
        # 숫자 하나 집어넣을 때 횟수 증가+검사하기
        hmSavingNum += 1
        if hmSavingNum == K:
            print(result[-1])
            quit()

    # 둘 중에 하나라도 다 옮겨 담았을 때
    if index1==len(array1):
        while index2<len(array2):
            result.append(array2[index2])
            hmSavingNum += 1
            if hmSavingNum == K:
                print(result[-1])
                quit()
            index2 += 1

    if index2==len(array2):
        while index1<len(array1):
            result.append(array1[index1])
            hmSavingNum += 1
            if hmSavingNum == K:
                print(result[-1])
                quit()
            index1 += 1

    # 전부 정렬했으나 입력받은 저장횟수가 전체 저장횟수보다 크면 -1 출력
    if len(result)==N and K > hmSavingNum:
        print(-1)
        return

    return result

mergeSort(arr)