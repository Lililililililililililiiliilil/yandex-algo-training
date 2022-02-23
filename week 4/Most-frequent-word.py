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
    else:
        prev_count[word] += 1

most_freq = (max(prev_count.values()))
for keys in prev_count.keys():
    if prev_count[keys] == most_freq:
        ans.append(keys)

print(min(ans))
