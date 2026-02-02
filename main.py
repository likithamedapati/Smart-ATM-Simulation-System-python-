print("Welcome to Smart ATM")
print("-" * 30)

correct_pin = "2310"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        print("Access granted ")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN  | Attempts left: {attempts}")

if attempts == 0:
    print("Too many failed attempts. Card blocked.")
    exit()
balance = 0
deposit_count = 0
withdraw_count = 0
transactions = []
while True:
    print("\n------ ATM MENU ------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Receipt")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
      try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount.")
        else:
            balance += amount
            deposit_count += 1
            transactions.append(f"Deposit: ₹{amount}")
            print(f"₹{amount} deposited successfully!")

      except:
        print("Invalid input.")


    elif choice == "2":
      try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            withdraw_count += 1
            transactions.append(f"Withdraw: ₹{amount}")
            print(f"₹{amount} withdrawn successfully!")

      except:
        print("Invalid input.")
    elif choice == "3":
        print(f"Current balance: ₹{balance:.2f}")

    elif choice == "4":
      
      print("\n--- Transaction History ---")

      if not transactions:
        print("No transactions yet.")
      else:
        for t in transactions:
            print(t)

      print(f"\nTotal deposits: {deposit_count}")
      print(f"Total withdrawals: {withdraw_count}")
      print(f"Current balance: ₹{balance:.2f}")

    elif choice == "5":
        print("Receipt selected")

    elif choice == "6":
        print("Thank you for using Smart ATM ")
        break

    else:
        print("Invalid choice, try again!")
