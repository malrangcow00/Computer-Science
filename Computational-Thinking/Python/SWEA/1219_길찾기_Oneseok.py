import sys
sys.stdin = open('SWEA.input/1219.txt', 'r')

try:
    while True:
        tc, N = map(int, input().split())
        list1 = list(map(int, input().split()))
        visited = [False for i in range(100)]
        arr = [[]for i in range(100)]
        for i in range(1, len(list1), 2):
            arr[list1[i-1]].append(list1[i])
        now = 0
        stack = []
        ans = 0
        while True:
            if now == 99:
                ans = 1
                break
            visited[now] = True
            got_next = False
            for a in arr[now]:
                if not visited[a]:
                    tmp = a
                    got_next = True
                    break
            if got_next:
                stack.append(now)
                now = tmp
            if not stack:
                break
            if not got_next:
                now = stack.pop()
        print(f'#{tc} {ans}')
except:
    pass