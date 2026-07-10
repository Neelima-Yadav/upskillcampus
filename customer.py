from database import get_connection

def register_customer():
    print("\n===== Customer Registration =====")

    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO customers(name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email)
        )
        conn.commit()
        print("\n✅ Customer Registered Successfully!")

    except Exception as e:
        print("\n❌ Error:", e)

    finally:
        conn.close()


def view_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    print("\n===== Customer List =====")

    if len(customers) == 0:
        print("No customers found.")
    else:
        for customer in customers:
            print(f"ID: {customer[0]}")
            print(f"Name: {customer[1]}")
            print(f"Phone: {customer[2]}")
            print(f"Email: {customer[3]}")
            print("-" * 30)

    conn.close()