total_bill = 0.00

while True:
    print("\n--- Coffee Shop Menu ---")
    print("1. Black Coffee - $2.50")
    print("2. Vanilla Latte - $4.00")
    print("3. Blueberry Muffin - $3.00")
    print("4. Complete Order (Checkout)")

    choice = input("Please select an option: ")

    if choice == "1":
        total_bill += 2.50
        print(f"Added Black Coffee. Current total: ${total_bill:.2f}")

    elif choice == "2":
        total_bill += 4.00
        print(f"Added Vanilla Latte. Current total: ${total_bill:.2f}")

    elif choice == "3":
        total_bill += 3.00
        print(f"Added Blueberry Muffin. Current total: ${total_bill:.2f}")

    elif choice == "4":
        print(f"Final total: ${total_bill:.2f}")
        break

    else:
        print("Invalid selection. Please choose a valid menu item.")