num_orders = int(input())

# ⦁    Price per capsule - a floating - point number in the range[0.01…100.00]
# ⦁    Days - integer in the range[1…31]
# ⦁    Capsules, needed per day - integer in the range[1…2000]
total = 0
price = 0
for orders in range(1, num_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule > 100 or price_per_capsule < 0.01:
        continue
    elif days > 31 or days < 1:
        continue
    elif capsules_per_day > 2000 or capsules_per_day < 1:
        continue
    else:
        price = price_per_capsule * days * capsules_per_day
        total = total + price
        print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")