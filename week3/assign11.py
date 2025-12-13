total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        value = line.strip()
        try:
            number = int(value)
            total += number
        except ValueError:
            continue

print("sum=", total)
