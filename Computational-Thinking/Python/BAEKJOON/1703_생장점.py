import sys
input = sys.stdin.readline

"""
문제가 무슨 말인지를 이해를 못해서 예제로 리버스엔지니어링을 하면...

3 0 2 0 2 0 은 그냥 0 빼고 모두 곱한 것

3 0 2 1 2 3은? ((3 - 0) * 2 - 1) * 2 - 3 = 7
"""

while True:
    branchorama = list(map(int, input().split()))
    if branchorama == [0]:
        break
    n = 1
    for i in range(branchorama[0]):
        splitting_factor = branchorama[2 * i + 1]
        p = branchorama[2 * i + 2]
        n = n * splitting_factor - p
    print(n)