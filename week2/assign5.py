sales_list = []

with open('sales.txt', 'r') as file:
    for line in file:
        value = line.strip()
        try:
            number = int(value)
            sales_list.append(number)
        except ValueError:
            continue


total_sales = sum(sales_list)

print("Valid sales:", sales_list)
print("Total sales", total_sales)
