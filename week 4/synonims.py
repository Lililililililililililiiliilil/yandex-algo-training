n = int(input())
syn = dict()

for i in range(n):
    key, value = input().split()
    syn[key] = value
    syn[value] = key

finder = input()
print(syn[finder])
