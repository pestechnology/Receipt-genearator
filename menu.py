def show_menu():
    menu = {
        1: ("Burger", 50),
        2: ("Pizza", 100),
        3: ("Sandwich", 40),
        4: ("Coffee", 30),
        5: ("gobi rice", 80)
    }

    print("\n--- FOOD MENU ---")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - Rs {value[1]}")

    return menu


def get_user_choice(menu):
    choice = int(input("Choose item number: "))
    quantity = int(input("Enter quantity: "))

    item_name, price = menu[choice]
    return item_name, price, quantity
