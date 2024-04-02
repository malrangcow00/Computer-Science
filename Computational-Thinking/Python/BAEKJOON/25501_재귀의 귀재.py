import sys
input = sys.stdin.readline

def recursion(word, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif word[l] != word[r]:
        return 0
    else:
        return recursion(word, l+1, r-1)

def isPalindrome(word):
    return recursion(word, 0, len(word) - 1)

N = int(input())
for _ in range(N):
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt)