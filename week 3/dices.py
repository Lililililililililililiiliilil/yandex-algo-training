n, m = map(int, input().split())

ann_dices = []
borya_dices = []

for i in range(n):
    ann_dices.append(int(input()))
for i in range(m):
    borya_dices.append(int(input()))

intersect = list(set(ann_dices).intersection(set(borya_dices)))
print(len(intersect))
print(*sorted(intersect))
only_ann = list(set(ann_dices).difference(set(borya_dices)))
print(len(only_ann))
print(*sorted(only_ann))
only_borya = list(set(borya_dices).difference(set(ann_dices)))
print(len(only_borya))
print(*sorted(only_borya))
