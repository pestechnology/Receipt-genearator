# main.py

from menu import show_menu, get_user_choice
from billing import calculate_subtotal, calculate_tax, calculate_total
from receipt import print_receipt
from storage import save_bill, view_previous_bills

def main():
    menu = show_menu()
    item, price, quantity = get_user_choice(menu)

    subtotal = calculate_subtotal(price, quantity)
    tax = calculate_tax(subtotal)
    total = calculate_total(subtotal, tax)

    print_receipt(item, quantity, price, subtotal, tax, total)
    save_bill(item, quantity, total)

    choice = input("\nView previous bills? (y/n): ")
    if choice.lower() == 'y':
        view_previous_bills()


if __name__ == "__main__":
    main()
