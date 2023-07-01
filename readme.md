In this project we'll imagine that we're programming the bill dispenser subsystem for an ATM.

A customer will enter the amount of money they want to withdraw from their account, and we need to write the program that will select which bills, and how many of each bill to give the user back, always optimizing by using the bills of largest denomination. The bills available are: $500, $100, $50, $25, $10, $5, $1.

For example, if the customer wants to withdraw $843, we should give them the following bills:

    $500:   1 bill
    $100:   3 bills
    $50:    0 bill
    $25:    1 bill
    $10:    1 bill
    $5:     1 bill
    $1:     3 bills

    Note: the customer can request withdraws amounts with dollar-precision: $1. So, $843 is a valid amount. This is probably not true for real ATMs.

The function calculate_bills_to_use() that returns a dictionary with the bill denomination and how many bills to use. Examples:

>>> calculte_bills_to_use(843)
{500: 1, 100: 3, 50: 0, 25: 1, 10: 1, 5: 1, 1: 3}

>>> calculte_bills_to_use(1763)
{500: 3, 100: 2, 50: 1, 25: 0, 10: 1, 5: 0, 1: 3}

>>> calculte_bills_to_use(177)
{500: 0, 100: 1, 50: 1, 25: 1, 10: 0, 5: 0, 1: 2}

>>> calculte_bills_to_use(355)
{500: 0, 100: 3, 50: 1, 25: 0, 10: 0, 5: 1, 1: 0}

>>> calculte_bills_to_use(10988)
{500: 21, 100: 4, 50: 1, 25: 1, 10: 1, 5: 0, 1: 3}
