denomination = [200, 100, 50, 20, 10, 5, 2, 1]


def teller(amount, denomination):
    result = {}

    for value in denomination:
        if amount >= value:
            amount = __prepare_banknotes_quantity(amount, value, result)
    return result


def __prepare_banknotes_quantity(amount, value, result):
    quantity = amount / value
    quantity = int(quantity)
    result[value] = quantity
    amount = amount - (value * quantity)
    return amount


print(teller(148, denomination))