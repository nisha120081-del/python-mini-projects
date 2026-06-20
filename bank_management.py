print("welcome to the bank management system")

print("first create an account")
name = input("Enter your name:")
balance = float(input("Enter your initial deposit amount:"))
print(f"Account created for {name} with initial balance of ${balance:.2f}")

i = 1
while i <= 4:
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        amount = float(input("Enter the amount to deposit:"))
        balance += amount
        print(f"Deposited ${amount:.2f}. New balance is ${balance:.2f}")
    elif choice == 2:
        amount = float(input("Enter the amount to withdraw:"))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${balance:.2f}")
    elif choice == 3:
        print(f"Current balance is ${balance:.2f}")
    elif choice == 4:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")

