# 최대한 리스트를 덜 생성하는 방식으로 진행하겠다...!
# 최대한 제자리 정렬 형태로 진행(like in-place sort...?)
def merge_sort(arr):
    # divide : 분할 처리하는 부분
    def divide(left, right):
        nonlocal arr
        if right - left < 2:
            return
        mid = (left + right) // 2
        divide(left, mid)
        divide(mid, right)
        merge(left, mid, right)
    # merge : 병합 처리하는 부분
    def merge(left, mid, right):
        nonlocal arr
        merged_arr = []
        i, j = left, mid

        while i < mid and j < right:
            if arr[i] < arr[j]:
                merged_arr.append(arr[i])
                i += 1
            else:
                merged_arr.append(arr[j])
                j += 1
        # 나머지 있는 요소들을 merged_arr에 추가...!
        merged_arr += arr[i:mid]
        merged_arr += arr[j:right]

        # 원본 배열 arr에 부여...!
        # for k in range(left, right):
        #     arr[k] = merged_arr[k - left]
        arr[left:right] = merged_arr
        # return arr

    # 리스트를 슬라이싱 방식으로 직접 새로운 리스트를 생성x
    # 인덱스(시작점, 끝점)를 전달하는 방식으로 진행하겠다
    right = 0
    left = len(arr) - 1
    return divide(right, left)

arr = [34,1,543,536,24,45,11,24,83,64,12,3,0,2]
sorted_arr = merge_sort(arr)
print(sorted_arr)