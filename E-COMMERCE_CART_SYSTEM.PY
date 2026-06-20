print("Welcome to Shopping Cart 🛒")

# Fixed products with prices
products = {
    "Shoes": 2000,
    "Shirt": 1000,
    "Bag": 1500,
    "Watch": 2500
}

cart = []

while True:
    print("\nAvailable Products:")
    for item in products:
        print(item, "-", products[item])

    print("\n1. Add Product")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Add product
    if choice == "1":
        name = input("Enter product name: ")

        if name in products:
            price = products[name]
            cart.append({"name": name, "price": price})
            print("Product added!")
        else:
            print("Product not found ❌")

    # View cart
    elif choice == "2":
        if cart:
            print("\nYour Cart:")
            for item in cart:
                print(item["name"], "-", item["price"])
        else:
            print("Cart is empty")

    # Checkout
    elif choice == "3":
        if cart:
            total = 0
            for item in cart:
                total += item["price"]

            print("Total bill:", total)

            if total > 1000:
                discount = total * 0.10
                total -= discount
                print("Discount:", discount)

            print("Final bill:", total)
        else:
            print("Cart is empty")

    # Exit
    elif choice == "4":
        print("Thank you for shopping! 🛍️")
        break

    else:
        print("Invalid choice")

