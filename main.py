
def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_discount(subtotal):
    if subtotal >= 5000:
        return subtotal * 0.20
    elif subtotal >= 2000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_final_bill(subtotal, discount):
    return subtotal - discount


def display_bill(product, price, quantity, subtotal, discount, final_bill):
    print("\n======= SHOPPING BILL =======")
    print("Product Name:", product)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Subtotal:", round(subtotal, 2))
    print("Discount:", round(discount, 2))
    print("Final Amount:", round(final_bill, 2))
    print("=============================")


def main():
    print("SHOPPING BILL CALCULATOR")

    product = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    subtotal = calculate_subtotal(price, quantity)
    discount = calculate_discount(subtotal)
    final_bill = calculate_final_bill(subtotal, discount)

    display_bill(product, price, quantity, subtotal, discount, final_bill)


if __name__ == "__main__":
    main()
