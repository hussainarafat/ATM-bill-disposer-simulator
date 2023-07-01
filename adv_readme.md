So far, we assumed infinite bills for each denomination, but we know that is not true. Let's modify our function so it receives a dictionary with the availability of the bills. For example, at the end of the day, we might run out of $100 bills, so we'll need to use as many bills of the following (in denomination) one ($50 in this case).

The function calculate_bills_to_use_advanced() that receives two parameters: the amount to withdraw, and a dictionary with bills and their availability. For example:

# There are no $100 bills
>>> calculate_bills_to_use_advanced(163, {
        500: 1,
        100: 0,
        50: 10,
        25: 10,
        10: 10,
        5: 10,
        1: 10
    })
{500: 0.0, 100: 0, 50: 3.0, 25: 0.0, 10: 1.0, 5: 0.0, 1: 3.0}

# There are no $100 or $10 bills
>>> calculate_bills_to_use_advanced(163, {
        500: 1,
        100: 0,
        50: 10,
        25: 10,
        10: 0,
        5: 10,
        1: 10
    })
{500: 0.0, 100: 0, 50: 3.0, 25: 0.0, 10: 0, 5: 2.0, 1: 3.0}
