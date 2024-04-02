# 활주로
def check(lst):
    global x,n

    # cnt_list 구성 [value, cnt] 저장
    cnt_lst = []
    cnt = 0
    value = lst[0]
    for k in range(n):
        if value == lst[k]:
            cnt += 1
        else:
            # 값 차이가 2 이상 날 경우, False(가지치기)
            if abs(value-lst[k])>1:
                return False
            cnt_lst.append([value,cnt])
            value = lst[k]
            cnt=1
    cnt_lst.append([value, cnt])

    # 양쪽 check
    m = len(cnt_lst)
    for i in range(m):

        # 3 2 2 2 2 3 을 체크하기 위함
        if 0<=i-1<m and 0<=i+1<m and cnt_lst[i][0]<cnt_lst[i-1][0] and cnt_lst[i][0]<cnt_lst[i+1][0] and cnt_lst[i][1]<x*2:
            return False

        # 그 외, 현위치와 양쪽 위치를 비교
        # 현위치 값이 크면 cnt 비교할 필요 없음
        # 현위치 값이 작을 때, cnt 비교하여 x값이 안되면 return False
        for di in [-1,1]:
            ni = i + di
            if 0<=ni<m:
                if cnt_lst[i][0]<cnt_lst[ni][0] and cnt_lst[i][1]<x:
                    return False
    return True



for t in range(int(input())):
    n,x = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    trans_arr = list(zip(*arr))
    ans = 0
    for i in range(n):
        if check(arr[i]):
            ans+=1
        if check(trans_arr[i]):
            ans+=1
    print(f'#{t+1} {ans}')