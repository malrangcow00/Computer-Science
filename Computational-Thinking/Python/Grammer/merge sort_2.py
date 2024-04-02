def merge_sort(arr):
    def merge(left_arr, right_arr):
        merged_arr = []
        i = j = 0 # 인덱스 변수 초기화

        # i 인덱스 또는 j 인덱스가 배열 범위를 넘은 경우 루프 종료...
        while i < len(left_arr) and j < len(right_arr):
            # i 인덱스가 가리키는 값 <-> j 인덱스가 가리키는 값을 비교
            if left_arr[i] < right_arr[j]:
                merged_arr.append(left_arr[i])
                i += 1
            else:
                merged_arr.append(right_arr[j])
                j += 1

        # 남아있는 리스트 요소들을 merged_arr 에 넣어주는 과정...
        merged_arr += left_arr[i:]
        merged_arr += right_arr[j:]
        return merged_arr


    if len(arr) == 1:
        return arr
    # 왼쪽 리스트와 오른쪽 리스트로 나눈다..
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

arr = [34,1,543,536,24,45,11,24,83,64,12,3,0,2]
sorted_arr = merge_sort(arr)
print(sorted_arr)