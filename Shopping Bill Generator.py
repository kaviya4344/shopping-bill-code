# Shopping Bill Generator

def calculate_bill(products):
    subtotal = 0

    print("\n========== SHOPPING BILL ==========")
    print(f"{'Product':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")
    print("-" * 43)

    for product in products:
        total = product["quantity"] * product["price"]
        subtotal += total

        print(f"{product['name']:<15}"
              f"{product['quantity']:<8}"
              f"{product['price']:<10.2f}"
              f"{total:<10.2f}")

    # Discount
    if subtotal >= 5000:
        discount_rate = 10
    elif subtotal >= 3000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount = subtotal * discount_rate / 100
    amount_after_discount = subtotal - discount

    # Tax
    tax_rate = 18
    tax = amount_after_discount * tax_rate / 100

    final_amount = amount_after_discount + tax

    print("-" * 43)
    print(f"Subtotal        : ₹{subtotal:.2f}")
    print(f"Discount ({discount_rate}%) : ₹{discount:.2f}")
    print(f"Tax ({tax_rate}%)      : ₹{tax:.2f}")
    print(f"Final Amount    : ₹{final_amount:.2f}")
    print("=" * 43)


# Store product details
products = []

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    product = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    products.append(product)

# Generate bill
calculate_bill(products)