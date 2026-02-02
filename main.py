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
