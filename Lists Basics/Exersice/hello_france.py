collection_items = input()
budget = float(input())

bought_products = []
new_prices = []

for item in collection_items.split('|'):
    tokens = item.split('->')
    product_type = tokens[0]
    product_price = float(tokens[1])
    if product_type == "Clothes" and product_price > 50.00:
        continue
    if product_type == "Shoes" and product_price > 35.00:
        continue
    if product_type == "Accessories" and product_price > 20.50:
        continue
    if budget >= product_price:
        budget -= product_price
        bought_products.append(product_price)
        new_prices.append(product_price * 1.4)

for new_price in new_prices:
    print(f'{new_price:.2f}', end=' ')
print('')

profit = sum(new_prices) - sum(bought_products)
print(f'Profit: {profit:.2f}')

new_budget = budget + sum(new_prices)
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")