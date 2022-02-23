sales = dict()
file = open('input.txt')
for lines in file:
    name, item, count = lines.split()
    count = int(count)
    if name in sales:
        if item in sales[name]:
            sales[name][item] += count
        else:
            sales[name][item] = count
    else:
        sales[name] = {item: count}

for name in sorted(sales):
    print(name + ':')
    for item in sorted(sales[name]):
        print(item, sales[name][item])
