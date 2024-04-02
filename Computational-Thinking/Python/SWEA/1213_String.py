for tc in range(1, 11):
    tcx = input()
    pattern = input()
    text = input()
    cnt = text.count(pattern)
    N = len(pattern)
    cnt = 0
    while pattern in text:
        cnt += 1
        text = text[text.index(pattern)+N:]
    print(f'#{tc} {cnt}')