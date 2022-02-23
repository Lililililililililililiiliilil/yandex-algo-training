def deposit(name, sum):
    bank_acc[name] = bank_acc.get(name, 0) + int(sum)


def withdraw(name, sum):
    bank_acc[name] = bank_acc.get(name, 0) - int(sum)


def balance(name):
    if name not in bank_acc:
        print('ERROR')
    else:
        print(bank_acc[name])


def transfer(name1, name2, sum):
    if name2 in bank_acc.keys():
        bank_acc[name1] -= sum
        bank_acc[name2] += sum
    else:
        bank_acc[name1] -= sum
        bank_acc[name2] = 0
        bank_acc[name2] += sum


def income(percent):
    for k, v in bank_acc.items():
        if v > 0:
            bank_acc[k] = int(v * ((int(percent) / 100) + 1))


bank_acc = dict()
file = open('input.txt')

for line in file:
    command = list(line.split())
    if command[0] == 'BALANCE':
        balance(command[1])
    elif command[0] == 'DEPOSIT':
        deposit(command[1], int(command[2]))
    elif command[0] == 'TRANSFER':
        transfer(command[1], command[2], int(command[3]))
    elif command[0] == 'WITHDRAW':
        withdraw(command[1], int(command[2]))
    elif command[0] == 'INCOME':
        income(int(command[1]))
file.close()
