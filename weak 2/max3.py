my_list = list(map(int, input().split()))

my_list.sort()

if my_list[-1] * my_list[-2] * my_list[-3] > my_list[0] * my_list[1] * my_list[-1]:
    print(my_list[-1], my_list[-2], my_list[-3])
else:
    print(my_list[0], my_list[1], my_list[-1])
