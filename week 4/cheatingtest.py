def wordCleaner(line):
    ans = []
    for c in line:
        if c.isalpha() or c.isdigit() or c == '_':
            ans.append(c)
        else:
            ans.append(' ')
    return ''.join(ans)


def isCorrect(word, startDig):
    if word.isdigit():
        return False
    if not word[0].isdigit() or startDig:
        return True
    return False


file = open('input.txt')

n, caseSens, startDig = file.readline().strip().split()
n = int(n)

caseSens = caseSens == 'yes'
startDig = startDig == 'yes'

keywords = set()

for _ in range(n):
    keyword = file.readline().strip()
    if not caseSens:
        keyword = keyword.lower()
    keywords.add(keyword)

cntPosId = {}

wordNumber = 0

for line in file.readlines():
    line = wordCleaner(line)
    words = line.strip().split()
    for word in words:
        if not caseSens:
            word = word.lower()
        if word in keywords:
            continue
        if isCorrect(word, startDig):
            wordNumber += 1
            if word not in cntPosId:
                cntPosId[word] = [0, wordNumber]
            cntPosId[word][0] += 1

bestWord = ''
maxCntPos = [0, 0]
for word in cntPosId:
    if cntPosId[word][0] > maxCntPos[0]:
        maxCntPos = cntPosId[word]
        bestWord = word
    if cntPosId[word][0] == maxCntPos[0] and cntPosId[word][1] < maxCntPos[1]:
        maxCntPos = cntPosId[word]
        bestWord = word
print(bestWord)
