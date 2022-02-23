a_1, b_1, a_2, b_2 = map(int, input().split())

if a_1 == a_2 and b_1 == b_2:
    print(a_1, b_2 + b_1)
elif a_1 == b_2 and b_1 == a_2:
    print(a_1, b_1 + a_2)
else:
    if b_1 > b_2 and a_1 > b_2:
        result = [(a_1 + b_2) * b_1, (b_1 + b_2) * a_1, (a_1 + a_2) * b_1, (b_1 + a_2) * a_1]
        min_ind = result.index(min(result))
        if min_ind == 0:
            print((a_1 + b_2), b_1)
        elif min_ind == 1:
            print((b_1 + b_2), a_1)
        elif min_ind == 2:
            print((a_1 + a_2), b_1)
        else:
            print((b_1 + a_2), a_1)
    else:
        result = [(a_1 + b_2) * b_2, (b_1 + b_2) * a_2, (a_1 + a_2) * b_2, (b_1 + a_2) * a_2]
        min_ind = result.index(min(result))
        if min_ind == 0:
            print((a_1 + b_2), b_2)
        elif min_ind == 1:
            print((b_1 + b_2), a_2)
        elif min_ind == 2:
            print((a_1 + a_2), b_2)
        else:
            print((b_1 + a_2), a_2)
