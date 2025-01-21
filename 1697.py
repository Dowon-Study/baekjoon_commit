import sys
from collections import deque

def hide_and_seek(N, K):
    max_position = 100000
    visited = [False] * (max_position + 1)
    queue = deque([(N, 0)])  # (현재 위치, 걸린 시간)

    while queue:
        current_position, time = queue.popleft()

        if current_position == K:
            return time

        next_positions = [current_position - 1, current_position + 1, current_position * 2]

        for next_position in next_positions:
            if 0 <= next_position <= max_position and not visited[next_position]:
                visited[next_position] = True
                queue.append((next_position, time + 1))

# 입력 처리
input_data = sys.stdin.read().strip()
N, K = map(int, input_data.split())

# 결과 출력
print(hide_and_seek(N, K))
