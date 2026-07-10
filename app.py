from customer import register_customer, view_customers

while True:
    print("\n========== FOOD DELIVERY SYSTEM ==========")
    print("1. Register Customer")
    print("2. View Customers")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_customer()

    elif choice == "2":
        view_customers()

    elif choice == "3":
        print("Thank you for using the Food Delivery System!")
        break

    else:
        print("Invalid choice! Please try again.")