def solution(n, computers):
    def DFS(i):
        visited[i] = True
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)

    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1

    return answer
