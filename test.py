def calculate_total(price, quantity):
    total = price * quantity
    print("Calculated Total:", total)

    if total > 1000:
        discount = total * 0.1

    return discount

calculate_total(500, 1)
