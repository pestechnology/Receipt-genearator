def save_bill(item, quantity, total):
    with open("bills.txt", "a") as file:
        file.write(f"{item} x{quantity} = Rs {total}\n")


def view_previous_bills():
    print("\n--- PREVIOUS BILLS ---")
    try:
        with open("bills.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No previous bills found.")
