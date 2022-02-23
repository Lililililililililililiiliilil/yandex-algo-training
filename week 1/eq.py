a = int(input())
b = int(input())
c = int(input())

if (a + b) == c ** 2 and (2 * a + b) == c ** 2:
    print('MANY SOLUTIONS')
elif a == 0 or c < 0:
    print('NO SOLUTION')
elif (c ** 2 - b) // a == (c ** 2 - b) / a:
    print((c ** 2 - b) // a)
else:
    print('NO SOLUTION')
