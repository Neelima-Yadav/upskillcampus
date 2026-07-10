cart = []

def add_to_cart():
    print("\n===== Add to Cart =====")

    item = input("Food Item: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    total = quantity * price

    cart.append({
        "item": item,
        "quantity": quantity,
        "price": price,
        "total": total
    })

    print("\n✅ Item Added to Cart!")

def view_cart():
    print("\n===== YOUR CART =====")

    if not cart:
        print("Cart is Empty!")
        return

    grand_total = 0

    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['item']}")
        print(f"   Quantity : {item['quantity']}")
        print(f"   Price    : ₹{item['price']}")
        print(f"   Total    : ₹{item['total']}")
        print("-" * 30)

        grand_total += item["total"]

    print(f"Grand Total : ₹{grand_total}")