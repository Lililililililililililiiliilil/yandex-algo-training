import sys

word = set()
for line in sys.stdin:
    word.update(line.split())
print(len(word))
