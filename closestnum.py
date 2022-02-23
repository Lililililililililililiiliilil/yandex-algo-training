n = int(input())
my_list = list(map(int, input().split()))
x = int(input())

ans = my_list[0]

for i in range(1, len(my_list)):
    if abs(my_list[i] - x) < abs(ans - x):
        ans = my_list[i]
print(ans)
