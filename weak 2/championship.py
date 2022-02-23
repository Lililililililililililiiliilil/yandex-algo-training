n = int(input())
my_list = list(map(int, input().split()))

max_score = my_list[0]

possible_scores = []

for i in range(len(my_list)):
    if my_list[i] > max_score:
        max_score = my_list[i]

max_index = my_list.index(max_score)

for i in range(1, len(my_list) - 1):
    if i > max_index and my_list[i] % 10 == 5 and my_list[i] > my_list[i + 1]:
        possible_scores.append(my_list[i])

if len(possible_scores) == 0:
    print(0)

else:

    my_list.sort(reverse=True)
    best_score_vasya = max(possible_scores)
    print(my_list.index(best_score_vasya) + 1)




