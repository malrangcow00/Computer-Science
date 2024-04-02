def solution(storey):
    answer = 0
    while storey:
        diff = storey % 10
        if diff < 5:
            answer += diff
        elif diff == 5:
            nxt = storey // 10
            if nxt % 10 >= 5:
                storey += 10
            answer += diff
        else:
            answer += (10 - diff)
            storey += 10
        storey //= 10
    return answer
