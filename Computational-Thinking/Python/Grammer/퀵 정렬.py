# 중간값을 pivot이라는 값으로 잡아서 분리
# 원본 배열을 그대로 이용하기 때문에 별도의 메모리가 필요하지 않다는 장점이 있다.

# 분할정복의 정복에 해당되는 코드
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin # 작은 값
    R = end # 큰 값
    while L < R:
        while(L<R and a[L] < a[pivot]) : L += 1
        while(L<R and a[R] >= a [pivot]) : R -= 1
        if L < R:
            if L == pivot :
                pivot = R
                a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R

