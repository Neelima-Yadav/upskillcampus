from database import get_connection
from cart import cart

def place_order():
    if not cart:
        print("\n❌ Your cart is empty!")
        return

    customer_id = int(input("\nEnter Customer ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    for item in cart:
        cursor.execute(
            """
            INSERT INTO orders (customer_id, item_name, quantity, total)
            VALUES (?, ?, ?, ?)
            """,
            (
                customer_id,
                item["item"],
                item["quantity"],
                item["total"]
            )
        )

    conn.commit()
    conn.close()

    cart.clear()

    print("\n✅ Order Placed Successfully!")


def view_orders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT orders.id,
               customers.name,
               orders.item_name,
               orders.quantity,
               orders.total
        FROM orders
        JOIN customers
        ON customers.id = orders.customer_id
    """)

    orders = cursor.fetchall()

    print("\n========== ORDER HISTORY ==========")

    if not orders:
        print("No orders found.")
    else:
        for order in orders:
            print(f"Order ID    : {order[0]}")
            print(f"Customer    : {order[1]}")
            print(f"Food Item   : {order[2]}")
            print(f"Quantity    : {order[3]}")
            print(f"Total Price : ₹{order[4]}")
            print("-" * 35)

    conn.close()