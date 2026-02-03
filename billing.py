def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_tax(subtotal):
    return subtotal * 0.05   # 5% tax


def calculate_total(subtotal, tax):
    return subtotal + tax
