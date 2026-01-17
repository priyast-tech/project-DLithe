# Billing Management System

products = {
    1: {"name": "Pen", "price": 10},
    2: {"name": "Notebook", "price": 50},
    3: {"name": "Pencil", "price": 5},
    4: {"name": "Eraser", "price": 3}
}

cart = []

def show_products():
    print("\nAvailable Products:")
    print("ID\tProduct\t\tPrice")
    for pid, details in products.items():
        print(f"{pid}\t{details['name']}\t\t{details['price']}")

def add_to_cart():
    pid = int(input("Enter Product ID: "))
    if pid in products:
        qty = int(input("Enter Quantity: "))
        cart.append({
            "name": products[pid]["name"],
            "price": products[pid]["price"],
            "quantity": qty
        })
        print("Product added to cart.")
    else:
        print("Invalid Product ID.")

def generate_bill():
    print("\n----- BILL RECEIPT -----")
    total = 0
    print("Product\tQty\tPrice\tAmount")
    for item in cart:
        amount = item["price"] * item["quantity"]
        total += amount
        print(f"{item['name']}\t{item['quantity']}\t{item['price']}\t{amount}")

    tax = total * 0.05  # 5% tax
    grand_total = total + tax

    print("\nSubtotal:", total)
    print("Tax (5%):", tax)
    print("Grand Total:", grand_total)
    print("------------------------")

def main():
    while True:
        print("\nBilling Management System")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. Generate Bill")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            if cart:
                generate_bill()
            else:
                print("Cart is empty.")
        elif choice == "4":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice.")

main()
