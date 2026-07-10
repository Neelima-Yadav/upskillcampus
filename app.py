from customer import register_customer, view_customers
from restaurant import add_restaurant, view_restaurants
while True:
    print("\n========== FOOD DELIVERY SYSTEM ==========")
    print("1. Register Customer")
    print("2. View Customers")
    print("3. Add Restaurant")
    print("4. View Restaurants")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_customer()

    elif choice == "2":
        view_customers()

    elif choice == "3":
        add_restaurant()

    elif choice == "4":
        view_restaurants()

    elif choice == "5":
        print("Thank you for using the Food Delivery System!")
        break

    else:
        print("Invalid choice! Please try again.")