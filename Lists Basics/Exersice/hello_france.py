collection = input()
budget = float(input())

collection_list = collection.split("|")

clothes_price = 50.00
shoes_price = 35.00
accessories_price = 20.50
saved_sum = 0
profit_sum = 0

list_buy = []

for x in collection_list:
    purchase = x.split("->")
    item = purchase[0]
    price = float(purchase[1])

    if (item == "Clothes" and price <= clothes_price and price <= budget) or (
            item == "Shoes" and price <= shoes_price and price <= budget) or \
            (item == "Accessories" and price <= shoes_price and price <= budget):
        budget -= price
        profit_price = price * 1.4
        saved_sum += profit_price
        list_buy.append(profit_price)
        profit_sum += profit_price - price
    else:
        continue

saved_sum = saved_sum + budget

for x in list_buy:
    print(f"{x:.2f}", end=" ")
print()
print(f"Profit: {profit_sum:.2f}")
if saved_sum >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
    profit_price = price * 1.4
    profit_sum += profit_price - price