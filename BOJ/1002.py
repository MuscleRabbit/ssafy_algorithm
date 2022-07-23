def calc_intersections():
    # 교점의 개수
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    distance_square = (x2 - x1) ** 2 + (y2 - y1) ** 2
    radius_add_square = (r1 + r2) ** 2
    radius_diff_square = (r1 - r2) ** 2

    if distance_square == radius_diff_square == 0:
        print(-1)
    elif distance_square == radius_add_square or distance_square == radius_diff_square:
        print(1)
    elif distance_square > radius_add_square or distance_square < radius_diff_square:
        print(0)
    else:
        print(2)

N = int(input())
for _ in range(N):
    calc_intersections()