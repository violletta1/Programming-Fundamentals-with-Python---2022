given_money = input().split(", ")
beggars = int(input())
starting_point = 0
current_beggar_sum = 0
given_money_digit = []
final_sum = []
for current_give_money in given_money:
    given_money_digit.append(int(current_give_money))

while starting_point < beggars:
    current_beggar_sum = 0
    for current_time_money_give in range(starting_point, len(given_money_digit), beggars):
        current_beggar_sum += given_money_digit[current_time_money_give]

    final_sum.append(current_beggar_sum)
    starting_point += 1

print(final_sum)