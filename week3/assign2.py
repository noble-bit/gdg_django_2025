def get_expensive_products(prices):

    expensive_items = []

    for price in prices:
        if price > 100:
            expensive_items.append(price)
    
    return expensive_items



prices = [120, 45, 300, 85, 150]

final_price = get_expensive_products(prices)
print(final_price)