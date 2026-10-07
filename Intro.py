count = 0
while count < 3:
    print("processing...") 
    count += 1

while True: #intetntional infinite loop
    cmd = input(("Type 'quit' to quit:"))
    if cmd == "quit": 
        print("shuttiong down.") 
    break 

#Autmatically loops 5 times (1,2,3,4,5)
for i in range(1,6):
    print("Current value of i is:", i)


while True:
    age = input("Enter your age: ")

    if age.isdigit():
        age = int(age)
        print("Age accepted!")
        break
    else:
        print("Invalid. Numbers only.")


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