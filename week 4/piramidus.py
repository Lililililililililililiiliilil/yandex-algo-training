n = int(input())
blocks = dict()

for i in range(n):
    w, h = map(int, input().split())
    if w in blocks.keys():
        blocks[w] = max(blocks[w], h)
    else:
        blocks[w] = h
print(sum(blocks.values()))
