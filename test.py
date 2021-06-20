
correct_pin = 3456
count = 0

while count < 3:
    supplied_pin = int(input("Enter your PIN: "))
    if supplied_pin != correct_pin:
        count += 1
        print(f"Incorrect PIN. Please Try Again. {count} attempt/s used.")
    elif supplied_pin == correct_pin:
        print("Success! You are now logged in")
        break