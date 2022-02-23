my_list = list(map(int, input().split()))

max1 = min(my_list[0], my_list[1])
max2 = max(my_list[1], my_list[0])

for i in range(2, len(my_list)):
    if my_list[i] > max2:
        max1 = max2
        max2 = my_list[i]
    elif my_list[i] > max1:
        max1 = my_list[i]

min1 = min(my_list[0], my_list[1])
min2 = max(my_list[1], my_list[0])

for i in range(2, len(my_list)):
    if my_list[i] < min1:
        min2 = min1
        min1 = my_list[i]
    elif my_list[i] < min2:
        min2 = my_list[i]

print(min1, min2)
print(max1, max2)

if min1 * min2 > max1 * max2:
    print(min1, min2)
else:
    print(max1, max2)
