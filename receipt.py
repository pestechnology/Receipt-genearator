# receipt.py

def print_receipt(item, quantity, price, subtotal, cgst, sgst, total):
    print("\n------ FOOD RECEIPT ------")
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: Rs {price}")
    print(f"\nSubtotal: Rs {subtotal}")
    print(f"cgst (2.5%): Rs {cgst}")
    print(f"sgst (2.5%): Rs {sgst}")
    print(f"Final Amount: Rs {total}")
    print("--------------------------")
