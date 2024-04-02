import sys
sys.stdin = open('input/1244.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # num: 숫자 cnt: 정해진 횟수
    num, cnt = input().split()
    cnt = int(cnt)
    num = list(map(int, list(num)))
    # 값, 인덱스 쌍 생성
    num = list([value, index] for index, value in enumerate(num))
    # 최대 상금을 표시하는 배열 복사
    pp = num[:]
    pp.sort(key=lambda x:x[1], reverse=True)
    pp.sort(key=lambda x:x[0], reverse=True)

    i = 0
    j = 0
    con = False
    while j < cnt:
        if list(value for value, index in num) == list(value for value, index in pp):
            break
        elif num[i] != pp[i]:
            # 같은 값이 여러개일 경우, 작은 값을 뒤에서부터 바꿔줄 필요가 있다.
            if i > 0 and pp[i][0] != pp[i-1][0]:
                con = False
            pri = list(value for value, index in num).count(pp[i][0])
            if pri > 1 and cnt - j > 1 and con == False:
            # if pri > 1 and con == False:
                num = num[:i] + sorted(num[i:i+pri], key=lambda x:x[0]) + num[i+pri:]
                con = True
            if pp[i][1] >= i:
                num[i], num[pp[i][1]] = num[pp[i][1]], num[i]
            else:
                tmp = num.index(pp[i])
                num[i], num[tmp] = num[num.index(pp[i])], num[i]
            i += 1
            j += 1
        else:
            i += 1

    # 문자열로 변환함과 동시에 인덱스 제거
    num = list(str(value) for value, index in num)

    if len(set(num)) != len(num):
        print(f'#{tc}', ''.join(num))
    else:
        if j < cnt:
            if (cnt - j) % 2 == 1:
                num[-1], num[-2] = num[-2], num[-1]
            print(f'#{tc}', ''.join(num))
        else:
            print(f'#{tc}', ''.join(num))