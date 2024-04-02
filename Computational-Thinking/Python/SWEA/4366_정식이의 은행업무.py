import sys
sys.stdin = open('input/4366.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bin = input()
    tri = list(input())
    bin_set = set()
    tri_set = set()
    for _ in range(len(bin)):
        bin_set.add(int(bin, 2)^2**_)
    for _ in range(len(tri)):
        for i in {'0', '1', '2'} - {tri[_]}:
            tmp = tri[:]
            tmp[_] = i
            tri_set.add(int(''.join(tmp), 3))
    print(f'#{tc}', *(bin_set & tri_set))

