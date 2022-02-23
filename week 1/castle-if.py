def sort2(a, b):
    if a > b:
        return b, a
    else:
        return a, b


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a, b = sort2(a, b)
b, c = sort2(b, c)
a, b = sort2(a, b)
d, e = sort2(d, e)

if d >= a and e >= b:
    print('YES')
else:
    print('NO')
