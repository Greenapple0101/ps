import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        grid[y][x] = 0

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == 1:
                    grid[ny][nx] = 0
                    q.append((nx, ny))

    count = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1:
                bfs(x, y)
                count += 1

    print(count)