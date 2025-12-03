try:
    with open("test1.txt", 'r') as f:
        file = f.read()
        print(file)

except Exception: 
    with open("text1.txt", "w") as f:
        f.write("Guest")
    
    with open("text1.txt", "r") as f:
        file = f.read()
        print(file)





