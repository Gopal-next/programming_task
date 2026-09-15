def calculate_total(price, quantity):
    total = price * quantity
    print("Total:", total)

    if total > 1000:
        discount = total * 0.1

    return discount
