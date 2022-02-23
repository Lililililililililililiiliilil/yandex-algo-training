n = int(input())

students = []

for i in range(n):
    m = int(input())
    languages = set()
    for j in range(m):
        languages.add(input())
    students.append(languages)
everyone = (set.intersection(*students))
at_least_one = (set.union(*students))
print(len(everyone))
for lg in everyone:
    print(lg)
print(len(at_least_one))
for lg in at_least_one:
    print(lg)
