try:
    with open("message.txt", "r") as file:
        for line in file:
            print(line.strip().upper())
except FileNotFoundError:
    print("Error: message.txt not found.")
