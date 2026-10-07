secret_pin = "8888"
attempts = 0

while attempts < 3:
    guess = input("Enter PIN: ")
    attempts += 1

    if guess == secret_pin:
        print("Correct PIN!")
        print("Balance: $1")
        break
    else:
        print("Incorrect PIN.")

if attempts == 3 and guess != secret_pin:
    print("Account Locked")