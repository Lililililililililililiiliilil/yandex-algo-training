s1 = input()
s2 = input()
uniq = set()
count = 0

for i in range(len(s2) - 1):
    uniq.add(s2[i:i + 2])

for i in range(len(s1) - 1):
    if s1[i:i + 2] in uniq:
        count += 1

print(count)
