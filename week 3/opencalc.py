x, y, z = map(int, input().split())

n = set(map(int, input()))

has_button = {x, y, z}

print(len(n.difference(has_button)))
