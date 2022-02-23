new_num = input()
first_given = input()
sec_given = input()
third_given = input()

numbers = [new_num, first_given, sec_given, third_given]

for i in range(4):
    numbers[i] = numbers[i].replace('(', '').replace(')', '').replace('-', '').replace('+', '')
    if len(numbers[i]) <= 7:
        numbers[i] = '495' + numbers[i]
    numbers[i] = numbers[i][-10:]

for i in range(1, 4):
    if numbers[i] == numbers[0]:
        print('YES')
    else:
        print('NO')
