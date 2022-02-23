my_list = list(map(int, input().split()))

check = False

for i in range(1, len(my_list)):
    if my_list[i - 1] >= my_list[i]:
        print('NO')
        check = True
        break
if not check:
    print("YES")
