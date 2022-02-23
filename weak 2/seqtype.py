def check_seq(seq):
    flag = 0
    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            flag += 1
    if flag == len(seq) - 1:
        return 'CONSTANT'
    flag = 0
    for i in range(len(seq) - 1):
        if seq[i] < seq[i + 1]:
            flag += 1
    if flag == len(seq) - 1:
        return 'ASCENDING'
    flag = 0
    for i in range(len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            flag += 1
    if flag == len(seq) - 1:
        return 'WEAKLY ASCENDING'
    flag = 0
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            flag += 1
    if flag == len(seq) - 1:
        return 'DESCENDING'
    flag = 0
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            flag += 1
    if flag == len(seq) - 1:
        return 'WEAKLY DESCENDING'
    return 'RANDOM'


numbers = []

num = int(input())
numbers.append(num)

while num != -2e9:
    num = int(input())
    numbers.append(num)

numbers.pop()

print(check_seq(numbers))
