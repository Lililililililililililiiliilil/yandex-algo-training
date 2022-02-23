file = open('input.txt')
text = list()
prev_count = dict()
ans = list()
for line in file:
    for word in line.split():
        text.append(word)
for word in text:
    if word not in prev_count:
        prev_count[word] = 1
        ans.append(0)
    else:
        ans.append(prev_count[word])
        prev_count[word] += 1

print(*ans)
