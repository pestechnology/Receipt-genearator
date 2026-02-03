from billing import calculate_subtotal, calculate_tax, calculate_total

def test_billing_calculation():
    subtotal = calculate_subtotal(50, 2)
    tax = calculate_tax(subtotal)
    total = calculate_total(subtotal, tax)

    assert subtotal == 100
    assert tax == 5.0
    assert total == 105.0
