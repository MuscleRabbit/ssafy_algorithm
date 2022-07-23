N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

# length = N, sum amount = M, max streak = K
i = 0
sum = 0
while i < M:
    j = 0
    while i < M and j < K:
        sum += arr[0]
        i += 1
        j += 1
    if not i < M:
        break
    sum += arr[1]
    i += 1

print(sum)