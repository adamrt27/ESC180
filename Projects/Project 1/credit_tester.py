# THIS IS A PROGRAM I MADE TO TEST CODE FOR THE CREDIT CARD ASSIGNMENT
# Run this program from the same directory as credit.py
# Nathan Chin is so cool

import math
from credit import *

''' my own tester function to help with testing '''
def test_case(num, expected, actual):
    if math.isclose(expected, actual):
        print(f"Passed case {num}")
    else:
        print(f"Failed case {num}")

if __name__ == '__main__':
    # NOTE - Checking owed with amount_owed() DOES change the latest update date

    # Test interest calculations (all same country, only purchases)
    print("TEST CASES 1 to 7 - interest calculations 1 (purchases only)")
    initialize()
    test_case("#1", 0, amount_owed(1, 1))
    test_case("#2", 0, amount_owed(7, 3))
    purchase(100, 7, 3, "Canada")
    test_case("#3", 100, amount_owed(7, 3))
    test_case("#4", 100, amount_owed(7, 4))
    test_case("#5", 121.550625, amount_owed(19, 8))
    purchase(40, 19, 8, "Canada")
    test_case("#6", 161.550625, amount_owed(20, 8))
    test_case("#7", 176.009564063, amount_owed(31, 10))
    
    # Test interest calculations (all same country, purchases and bill payments)
    print("\nTEST CASES 8 to 15 - interest calculations 2 (purchases, bill payments)")
    initialize()
    purchase(50, 10, 2, "Canada")
    pay_bill(40, 11, 2)
    test_case("#8", 10, amount_owed(11, 2))
    test_case("#9", 10.5, amount_owed(1, 4))
    purchase(90, 1, 4, "Canada")
    test_case("#10", 100.5, amount_owed(1, 4))
    test_case("#11", 116.949065625, amount_owed(1, 8))
    pay_bill(50, 1, 8)
    test_case("#12", 66.949065625, amount_owed(1, 8))
    purchase(100, 1, 9, "Canada")
    test_case("#13", 170.2965189063, amount_owed(1, 9))
    pay_bill(50, 1, 9)
    test_case("#14", 120.2965189063, amount_owed(1, 9))
    test_case("#15", 133.745757699, amount_owed(31, 12))

    # Test disabled card logic
    print("\nTEST CASES 16 to 20 - disabled card logic")
    initialize()
    purchase(100, 1, 1, "Canada")
    test_case("#16", 100, amount_owed(1, 1))
    purchase(100, 1, 1, "France")
    test_case("#17", 200, amount_owed(1, 1))
    purchase(100, 1, 1, "Canada")
    test_case("#18", 300, amount_owed(1, 1))
    purchase(100, 1, 1, "China") # card disabled
    test_case("#19", 300, amount_owed(1, 1))
    purchase(100, 1, 1, "Canada")
    test_case("#20", 300, amount_owed(1, 1))

    # Test input with invalid dates
    print("\nTEST CASES 21 to 25 - input with invalid dates")
    initialize()
    purchase(100, 10, 5, "Canada")
    purchase(100, 1, 4, "Canada")
    test_case("#21", 100, amount_owed(10, 5))
    purchase(100, 5, 5, "Canada")
    test_case("#22", 100, amount_owed(10, 5))
    purchase(75, 10, 5, "France")
    purchase(75, 3, 2, "Japan") # card disabled (according to prof)
    purchase(100, 20, 5, "Canada")
    test_case("#23", 175, amount_owed(20, 5))
    amount_owed(20, 10)
    purchase(100, 20, 5, "Canada")
    test_case("#24", 212.71359375, amount_owed(20, 10))
    test_case("#25", 1, int(amount_owed(20, 8) == "error"))

    # Test interest calculations (edge cases)
    print("\nTEST CASES 26 to 30 - interest calculations 3 (edge cases)")
    initialize()
    purchase(100, 1, 1, "Canada")
    purchase(100, 1, 2, "Canada")
    test_case("#26", 200, amount_owed(1, 2))
    purchase(100, 1, 3, "Canada")
    test_case("#27", 305, amount_owed(1, 3))
    pay_bill(250, 1, 3)
    test_case("#28", 55, amount_owed(1, 3))
    test_case("#29", 57.75, amount_owed(1, 5))
    purchase(42.25, 1, 5, "Canada")
    pay_bill(100, 1, 5)
    test_case("#30", 0, amount_owed(1, 8))

