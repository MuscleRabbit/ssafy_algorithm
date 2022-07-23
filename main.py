T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    ans = [[0] * 3 for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    for j in range(N):
        temp = str()
        for i in range(N-1, -1, -1):
            temp += str(arr[i][j])
        ans[j][0] = temp

    for i in range(N-1, -1, -1):
        temp = str()
        for j in range(N-1, -1, -1):
            temp += str(arr[i][j])
        ans[N - 1 - i][1] = temp

    for j in range(N-1, -1, -1):
        temp = str()
        for i in range(N):
            temp += str(arr[i][j])
        ans[N - 1 - j][2] = temp

    print("#{}".format(tc))
    for i in range(N):
        for j in range(3):
            print(ans[i][j], end='')
            if j == 2:
                print('\n', end = '')
            else:
                print(' ', end = '')