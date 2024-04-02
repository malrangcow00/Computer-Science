
arr = [1, 5, 7, 43, 76, 2, 3, 5, 3, 6, 1]

# 최댓값에 해당하는 요소 인덱스를 반환하여라
mx = arr[0]
max_i = 0
for idx in range(len(arr)):
    if mx < arr[idx]:
        mx = arr[idx]
        max_i = idx
print(mx, max_i)

mx = arr[0]
max_i = 0
for idx, val in enumerate(arr):
    if mx < val:
        mx = val
        max_i = idx
print(mx, max_i)

print(*enumerate(arr)) # 튜플로 인덱스 값을 같이 가져온다

idx, val = max(enumerate(arr), key = lambda x: x[1]) # N
print(val)
print(idx)
