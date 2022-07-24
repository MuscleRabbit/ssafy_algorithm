K, N = map(int, input().split())

prepared = [0] * K
for i in range(K):
    prepared[i] = int(input())

prepared.sort()
unit_max = prepared[0]
unit_min = 0
while True:
    cnt = 0
    unit_now = (unit_max + unit_min) // 2
    if unit_now == unit_min:
        break
    for i in range(K):
        cnt += prepared[i] // unit_now
    if cnt < N:
        unit_max = unit_now
    else:
        unit_min = unit_now

print(unit_now)