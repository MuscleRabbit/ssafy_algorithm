input_data = input()
# a ~ h & 1 ~ 8
x = 'abcdefgh'.find(input_data[0])
y = '12345678'.find(input_data[1])

steps = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, -2), (2, -1)]

cnt = 0
for step in steps:
    if 0 <= x + step[0] < 8 and 0 <= y + step[1] < 8:
        cnt += 1

print(cnt)