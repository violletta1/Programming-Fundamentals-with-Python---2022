group_size = int(input())
days = int(input())
companions_num = group_size
earn_coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        companions_num -= 2
    if current_day % 15 == 0:
        companions_num += 5
    if current_day % 5 == 0:
        earn_coins += 20 * companions_num
        if current_day % 3 == 0:
            earn_coins -= 2 * companions_num
    if current_day % 3 == 0:
        earn_coins -= 3 * companions_num


    earn_coins += 50
    earn_coins -= 2 * companions_num

earn_coins_per_companion = earn_coins / companions_num
print(f"{companions_num} companions received {int(earn_coins_per_companion)} coins each.")

# Note: You cannot split a coin, so you should round down the coins to an integer number.
