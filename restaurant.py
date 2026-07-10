from database import get_connection

def add_restaurant():
    print("\n===== Add Restaurant =====")

    name = input("Restaurant Name: ")
    location = input("Location: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO restaurants(name, location) VALUES (?, ?)",
        (name, location)
    )

    conn.commit()
    conn.close()

    print("\n✅ Restaurant Added Successfully!")

def view_restaurants():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM restaurants")
    restaurants = cursor.fetchall()

    print("\n===== Restaurant List =====")

    if not restaurants:
        print("No restaurants available.")
    else:
        for restaurant in restaurants:
            print(f"ID: {restaurant[0]}")
            print(f"Name: {restaurant[1]}")
            print(f"Location: {restaurant[2]}")
            print("-" * 30)

    conn.close()