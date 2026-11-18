# Restaurant Billing System
# PS No. 38 | Python 3

menu = {
    "Dosa": 80,
    "Idli": 40,
    "Thali": 150,
    "Tea": 20
}

orders = []

print("=" * 45)
print("          RESTAURANT BILLING SYSTEM")
print("=" * 45)
print("\nMenu:")
for item, price in menu.items():
    print(f"{item:<10} Rs. {price}")

print("\nEnter items one by one. Type 'done' to generate bill.")

while True:
    item_name = input("\nOrder item: ").strip().title()

    if item_name.lower() == "done":
        break

    if item_name not in menu:
        print("Item not on the menu. Available: Dosa, Idli, Thali, Tea.")
        continue

    quantity_input = input("Quantity: ").strip()

    try:
        quantity = int(quantity_input)
        if quantity < 1:
            print("Quantity must be at least 1.")
            continue
    except ValueError:
        print("Invalid quantity. Enter a whole number.")
        continue

    amount = menu[item_name] * quantity
    orders.append({
        "item": item_name,
        "quantity": quantity,
        "amount": amount
    })
    print(f"{item_name} x{quantity} added | Amount: {amount}")

if not orders:
    print("\nNo items ordered. No bill generated.")
else:
    subtotal = sum(order["amount"] for order in orders)

    discount = subtotal * 0.10 if subtotal > 500 else 0
    discounted_amount = subtotal - discount
    gst = discounted_amount * 0.05
    grand_total = discounted_amount + gst

    print("\n" + "=" * 45)
    print("                 FINAL BILL")
    print("=" * 45)
    print(f"{'Item':<12}{'Qty':<6}{'Amount (Rs.)':>15}")
    print("-" * 45)

    for order in orders:
        print(f"{order['item']:<12}{order['quantity']:<6}{order['amount']:>15.2f}")

    print("-" * 45)
    print(f"{'Subtotal:':<28} Rs. {subtotal:.2f}")
    print(f"{'Discount (10%):':<28} Rs. {discount:.2f}")
    print(f"{'GST (5%):':<28} Rs. {gst:.2f}")
    print(f"{'Grand Total:':<28} Rs. {grand_total:.2f}")
    print("=" * 45)
    print("       Thank you! Visit again.")
