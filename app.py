from customer import register_customer, view_customers
from restaurant import add_restaurant, view_restaurants
from menu import add_menu_item, view_menu
from cart import add_to_cart, view_cart
from order import place_order, view_orders

while True:
    print("\n========== FOOD DELIVERY SYSTEM ==========")
    print("1. Register Customer")
    print("2. View Customers")
    print("3. Add Restaurant")
    print("4. View Restaurants")
    print("5. Add Menu Item")
    print("6. View Menu")
    print("7. Add to Cart")
    print("8. View Cart")
    print("9. Place Order")
    print("10. View Orders")
    print("11. Exit")

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
        add_menu_item()

    elif choice == "6":
        view_menu()

    elif choice == "7":
        add_to_cart()

    elif choice == "8":
        view_cart()

    elif choice == "9":
        place_order()

    elif choice == "10":
        view_orders()

    elif choice == "11":
        print("\nThank you for using the Food Delivery System!")
        break

    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 11.")