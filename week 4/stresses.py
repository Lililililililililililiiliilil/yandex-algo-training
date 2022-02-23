n = int(input())

dict = dict()

for _ in range(n):
    word = input()
    wordLow = word.lower()
    if wordLow not in dict:
        dict[wordLow] = set()
    dict[wordLow].add(word)
sentence = input()

mistakes = 0

for word in sentence.split():
    if word.lower() in dict:
        if word in dict[word.lower()]:
            continue
        else:
            mistakes += 1
    else:
        upperCount = 0
        for char in word:
            if char.isupper():
                upperCount += 1
        if upperCount != 1:
            mistakes += 1

print(mistakes)
