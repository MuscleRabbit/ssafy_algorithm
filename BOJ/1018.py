N, M = map(int, input().split())

board = list()
for _ in range(N):
    board.append(input())

change_min = int(1e9)
for i in range(N-8 + 1):
    for j in range(M-8 + 1):
        start = board[i][j]
        change_cnt = 0
        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0 and board[i+k][j+l] == start:
                    continue
                elif (k + l) % 2 != 0 and board[i+k][j+l] != start:
                    continue
                else:
                    change_cnt += 1
        change_min = min(change_min, change_cnt)
        change_cnt = 0
        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0 and board[i+k][j+l] != start:
                    continue
                elif (k + l) % 2 != 0 and board[i+k][j+l] == start:
                    continue
                else:
                    change_cnt += 1
        change_min = min(change_min, change_cnt)

print(change_min)