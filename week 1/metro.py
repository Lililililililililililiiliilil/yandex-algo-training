a = int(input())
b = int(input())
n = int(input())
m = int(input())

first_min = a * (n - 1) + n
first_max = a * (n - 1) + n + 2 * a
second_min = b * (m - 1) + m
second_max = b * (m - 1) + m + 2 * b

if max(first_min, second_min) > min(first_max, second_max):
    print(-1)
else:
    print(max(first_min, second_min), min(first_max, second_max))
