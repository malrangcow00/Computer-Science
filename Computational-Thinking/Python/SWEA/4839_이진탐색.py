T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    l = 1
    r = P
    c = (l+r)//2
    cnt = 0
    while c != A:
        if A > c:
            l = c
            c = (l+r)//2
            cnt += 1
        else:
            r = c
            c = (l+r)//2
            cnt += 1

    l = 1
    r = P
    c = (l+r)//2
    while c != B:
        if B > c:
            l = c
            c = (l+r)//2
            cnt -= 1
        else:
            r = c
            c = (l+r)//2
            cnt -= 1

    # 결과는 반대로 
    if cnt < 0:
        print(f'#{tc} A')
    elif cnt > 0:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')