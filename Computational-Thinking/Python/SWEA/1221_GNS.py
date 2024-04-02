import sys
sys.stdin = open('input/1221.txt', 'r')
# sys.stdout = open('output/test.txt', 'w')

# 기존 배열을 텍스트로 변환 후 정렬
trans = {
    'ZRO' : '0',
    'ONE' : '1',
    'TWO' : '2',
    'THR' : '3',
    'FOR' : '4',
    'FIV' : '5',
    'SIX' : '6',
    'SVN' : '7',
    'EGT' : '8',
    'NIN' : '9'
}

T = int(input())
for tc in range(1, T+1):
    input()
    arr = input()
    for _ in trans.keys():
        arr = arr.replace(_, trans[_])
    arr = arr.split()
    arr.sort()
    arr = ' '.join(arr)
    cnt_rev = {v:k for k,v in trans.items()}
    for _ in cnt_rev.keys():
        arr = arr.replace(_, cnt_rev[_])
    print(tc)
    print(arr)



# # 딕셔너리를 이용한 계수정렬
# T = int(input())
# for tcx in range(T):
#
#     cnt = {
#         'ZRO' : 0,
#         'ONE' : 0,
#         'TWO' : 0,
#         'THR' : 0,
#         'FOR' : 0,
#         'FIV' : 0,
#         'SIX' : 0,
#         'SVN' : 0,
#         'EGT' : 0,
#         'NIN' : 0
#     }
#
#     tc, N = input().split()
#     arr = input().split()
#     for _ in arr:
#         cnt[_] += 1
#     print(tc)
#     for _ in cnt:
#         for i in range(cnt[_]):
#             print(_, end=' ')
#     print()


# # count 메서드 사용
# T = int(input())
# for tcx in range(T):
#     tc, N = input().split()
#     arr = input().split()
#     txt = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     print(tc)
#     for _ in txt:
#         for i in range(arr.count(_)):
#             print(_, end = ' ')