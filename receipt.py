# receipt.py

def print_receipt(item, quantity, price, subtotal, tax, total):
    print("\n------ FOOD RECEIPT ------")
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: Rs {price}")
    print(f"\nSubtotal: Rs {subtotal}")
    print(f"Tax (5%): Rs {tax}")
    print(f"Final Amount: Rs {total}")
    print("--------------------------")

