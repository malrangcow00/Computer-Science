def backtrack(a, k, i):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    if k == i:
        process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, i, c)
        for j in range(ncandidates):
            a[k] = c[j]
            backtrack(a, k, i)

def process_solution(a, k):
    global ans
    tmp = []
    for i in range(1, k+1):
        tmp.append(int(a[i]))
    ans.append(tmp)

def construct_candidates(a, k, i, c):
    c[0] = True
    c[1] = False
    return 2


MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
ans = []
backtrack(a, 0, 3)
print(*ans)