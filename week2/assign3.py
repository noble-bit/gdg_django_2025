def logged_user_activity():
    
    with open("log.txt", 'a') as file:
        file.write("User logged in\n")
    
    with open("log.txt", "r") as file:
        logs = file.read()
    
    print("------LOG HISTORY-----")
    print(logs)

logged_user_activity()