t_room, t_cond = map(int, input().split())
mode = input()
if mode == 'fan':
    print(t_room)
elif mode == 'auto':
    print(t_cond)
elif mode == 'freeze':
    if t_room > t_cond:
        print(t_cond)
    else:
        print(t_room)
elif mode == 'heat':
    if t_room < t_cond:
        print(t_cond)
    else:
        print(t_room)
