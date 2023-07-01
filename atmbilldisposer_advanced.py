def calculate_bills_to_use_advanced(amount, bills):
    result = {}
    for bill,available in bills.items():
        count = (amount - (amount % bill)) / bill
        count = min(count, available)
        result[bill] = count
        amount -= (bill * count)
    return result