def get_price(item, quantity):
    item = item.lower()  # normalize input

    if item == "tea":
        return 10 * quantity
    elif item == "coffee":
        return 15 * quantity
    elif item == "snacks":
        return 20 * quantity
    elif item == "lunch":
        return 50 * quantity
    else:
        return None  # invalid item


def canteen():
    print("Hello, Welcome to the College Canteen")
    print("Menu:")
    print("Tea - ₹10")
    print("Coffee - ₹15")
    print("Snacks - ₹20")
    print("Lunch - ₹50")

    total = 0

    while True:
        item = input("\nEnter item name: ")

        try:
            quantity = int(input("Enter quantity: "))
        except:
            print("Invalid quantity. Please enter a number.")
            continue

        cost = get_price(item, quantity)

        if cost is None:
            print("Item not available. Please choose from menu.")
            continue

        total += cost
        print(f"Current bill: ₹{total}")

        more = input("Do you want more items? (Y/N): ").lower()
        if more != "y":
            break

    # Discount logic
    discount = 0
    if total > 100:
        discount = total * 0.10

    final_amount = total - discount

    print("\n------ BILL RECEIPT ------")
    print(f"Total Bill      : ₹{total}")
    print(f"Discount (10%)  : ₹{discount}")
    print(f"Final Payable   : ₹{final_amount}")
    print("Thank you for visiting!")


canteen()
