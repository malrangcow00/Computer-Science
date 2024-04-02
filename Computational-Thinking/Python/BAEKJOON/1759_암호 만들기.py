import sys
input = sys.stdin.readline

def comb(password, i, vowel_count, consonant_count):
    if len(password) == L:
        if vowel_count >= 1 and consonant_count >= 2:
            cases.append(''.join(password))
        return

    if i >= C:
        return

    if letters[i] in 'aeiou':
        comb(password + [letters[i]], i + 1, vowel_count + 1, consonant_count)
    else:
        comb(password + [letters[i]], i + 1, vowel_count, consonant_count + 1)

    comb(password, i + 1, vowel_count, consonant_count)

L, C = map(int, input().split())

letters = sorted(input().rstrip().split())

cases = []
comb([], 0, 0, 0)
cases = sorted(list(set(cases)))
for case in cases:
    print(case)
