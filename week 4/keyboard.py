n = int(input())
max_click = list(map(int, input().split()))

k = int(input())
clicks = list(map(int, input().split()))

for click in clicks:
    max_click[click - 1] -= 1

for click in max_click:
    if click < 0:
        print('YES')
    else:
        print("NO")
