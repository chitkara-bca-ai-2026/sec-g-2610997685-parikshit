stock_list = ["Pencil", "Marker", "Stapler", "Folder"]

while True:
    print("\n" + "=" * 34)
    print("       STOCK MANAGEMENT SYSTEM")
    print("=" * 34)

    print("1. View Stock")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Sort Stock")
    print("5. Exit")

    option = input("\nEnter your option (1-5): ")

    if option == "1":
        print("\n--- Current Stock ---")
        if len(stock_list) == 0:
            print("Stock is empty.")
        else:
            for product in stock_list:
                print("-", product)

    elif option == "2":
        product = input("Enter product name to add: ")

        if product.strip() != "":
            stock_list.append(product)
            print(f"[SUCCESS] '{product}' added to stock.")
        else:
            print("Error: Product name cannot be empty.")

    elif option == "3":
        product = input("Enter product name to remove: ")

        if product in stock_list:
            stock_list.remove(product)
            print(f"[SUCCESS] '{product}' removed from stock.")
        else:
            print(f"Error: '{product}' not found in stock.")

    elif option == "5":
        print("thank you for using the stock management system")
        break
    else:
        print("invalid option! please enter a valid number from 1 to 5.")
