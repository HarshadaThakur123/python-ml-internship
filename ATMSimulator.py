balance = 1000  # Starting balance
correct_pin = "1234"

# Ask for PIN
pin = input("Enter your PIN: ")
if pin != correct_pin:
    print("Incorrect PIN. Access denied.")
else:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your balance is ₹{balance}")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"₹{amount} deposited.")
                else:
                    print("Enter a positive amount.")
            except:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Not enough balance.")
                elif amount <= 0:
                    print("Enter a positive amount.")
                else:
                    balance -= amount
                    print(f"₹{amount} withdrawn.")
            except:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
