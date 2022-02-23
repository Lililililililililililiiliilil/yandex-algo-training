def make_field(n, m, mines):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    field = []

    for i in range(n + 2):
        field.append([0] * (m + 2))

    for mineX, mineY in mines:
        for k in range(len(dx)):
            field[mineX + dx[k]][mineY + dy[k]] += 1

    for mineX, mineY in mines:
        field[mineX][mineY] = '*'

    return field


n, m, k = map(int, input().split())
mines = []

for i in range(k):
    mines.append(tuple(map(int, input().split())))

my_field = make_field(n, m, mines)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(my_field[i][j], end=' ')
    print()
