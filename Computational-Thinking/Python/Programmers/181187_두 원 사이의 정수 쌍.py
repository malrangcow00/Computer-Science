def included(x, y, r1, r2):
    return r1**2 <= x**2 + y**2 <= r2**2


def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        for y in range(r2+1):
            if included(x, y, r1, r2):
                answer += 1
    return answer * 4

# print(solution(2, 3))
