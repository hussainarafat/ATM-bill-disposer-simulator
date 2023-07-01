def calculate_bills_to_use(amount):
    bills = [500, 100, 50, 25, 10, 5, 1]
    result = {}
    for bill in bills:
        count = (amount - (amount % bill)) / bill
        result[bill] = count
        amount -= (bill * count)
    return result