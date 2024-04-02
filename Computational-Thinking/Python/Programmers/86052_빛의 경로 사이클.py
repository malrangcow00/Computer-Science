def solution(grid):
    answer = []
    width, height = len(grid[0]), len(grid)

    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)

    visited = [[[False] * 4 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            for i in range(4):
                if not visited[y][x][i]:
                    # 이동 횟수
                    cnt = 0
                    nx, ny = x, y
                    while not visited[ny][nx][i]:
                        visited[ny][nx][i] = True
                        cnt += 1
                        if grid[ny][nx] == "L":
                            i = (i - 1) % 4
                        elif grid[ny][nx] == "R":
                            i = (i + 1) % 4

                        # 격자 밖으로 나가면 ...
                        ny = (ny + dy[i]) % height
                        nx = (nx + dx[i]) % width
                    answer.append(cnt)
    answer.sort()
    return answer
