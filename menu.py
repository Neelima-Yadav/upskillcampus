from database import get_connection

def add_menu_item():
    print("\n===== Add Menu Item =====")

    restaurant_id = int(input("Restaurant ID: "))
    item_name = input("Food Item: ")
    price = float(input("Price: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO menu (restaurant_id, item_name, price) VALUES (?, ?, ?)",
        (restaurant_id, item_name, price)
    )

    conn.commit()
    conn.close()

    print("\n✅ Menu Item Added Successfully!")


def view_menu():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT restaurants.name, menu.item_name, menu.price
        FROM menu
        JOIN restaurants
        ON restaurants.id = menu.restaurant_id
    """)

    items = cursor.fetchall()

    print("\n===== FOOD MENU =====")

    if not items:
        print("No menu items available.")
    else:
        for item in items:
            print(f"Restaurant : {item[0]}")
            print(f"Food Item  : {item[1]}")
            print(f"Price      : ₹{item[2]}")
            print("-" * 30)

    conn.close()