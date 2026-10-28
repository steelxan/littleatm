pin = "1234"
balance = 1000
attempts = 0
max_attempts = 3
logged_in = False

while attempts < max_attempts:
    entered = input("Enter password: ")

    if entered == pin:
        print("Login successfully")
        logged_in = True
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print("Wrong password.", remaining, "chances left")

        if attempts == max_attempts:
            print("You have been blocked")

if logged_in:
    while True:
        print("1 - Balance") 
        print("2 - Withdraw")
        print("3 - Deposit") 
        print("4 - Exit")

        choice = input("Selection: ")

        if choice == "1":
            print(f"Your balance: {balance}")

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                print(f"Withdrawn: {amount}")
                print(f"New balance: {balance}")

        elif choice == "3":
            amount = int(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Invalid amount")
            else:
                balance += amount
                print(f"Deposited: {amount}")
                print(f"New balance: {balance}")

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid selection")