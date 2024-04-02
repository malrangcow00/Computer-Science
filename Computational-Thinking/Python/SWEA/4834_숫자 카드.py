T = int(input())

for i in range(1, T+1):
    N = int(input())
    card_dict = {}
    card = input()
    for j in card:
        if j not in card_dict.keys():
            card_dict[j] = 0
        card_dict[j] += 1
    card_dict = dict(sorted(card_dict.items()))
    # 딕셔너리 정렬에 의해서 자동으로 숫자가 더 큰 값이 최댓값 항목으로 덧씌워진다.
    cnt = max(list(card_dict.values()))
    card_re = {v:k for k,v in card_dict.items()}
    card_max = card_re.get(cnt)
    print(f'#{i} {card_max} {cnt}')