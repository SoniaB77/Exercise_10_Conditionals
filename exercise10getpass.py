import getpass

correct_pin = 3456
count = 0

while count < 3:
    supplied_pin = int(getpass.getpass("Enter your PIN: "))
    if supplied_pin != correct_pin:
        count += 1
        print("Incorrect PIN. Please Try Again. " + str(count) + " attempt/s used.")
    elif supplied_pin == correct_pin:
        print("Success! You are now logged in")
        break

