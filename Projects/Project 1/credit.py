# Intialize all required variables for the credit card simulation.

def initialize():
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_country, last_country2
    global last_update_month, last_update_day
    global purchase_history
    global card_disabled

    last_update_month = -1
    last_update_day = -1

    card_disabled = False

    purchase_history = []
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_country = None
    last_country2 = None    


# Return True if the date given by integers day1 and month1
# is the same as, or later than the date given by day2 and 
# month2.

def date_same_or_later(day1, month1, day2, month2):
    if month1 > month2:
        return True
    elif month1 ==  month2:
        if day1 >= day2:
            return True
        else:
            return False
    else:
        return False
    

# Return true if strings c1, c2 and c3 are different from
# each other.

def all_three_different(c1, c2, c3):
    if c1 != None and c2 != None and c3 != None:
        if c1 !=  c2 and c2 != c3 and c3 != c1:
            return True
        else:
            return False

# Disable card when the last 3 purchases (including the current
# one) have been in 3 different countries.

def fraud_detector(country):
    global last_country, last_country2, card_disabled
    if all_three_different(country, last_country, last_country2):
        card_disabled = True


# Return "error" when a purchase has been made at a date later 
# than (day, month).

def error_detector(day, month):
    global last_update_day, last_update_month
    if date_same_or_later(last_update_day-1,last_update_month, day, month):
        return True


# Recalculate current amounts owed and their interest. This function also updates
# the interest on each purchase.

def interest_calculator(month):
    global purchase_history, cur_balance_owing_intst, cur_balance_owing_recent
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    for i in range(len(purchase_history)):
        month_pur = purchase_history[i][2]
        if month_pur == month or month_pur + 1 == month:
            cur_balance_owing_recent += float(purchase_history[i][0])
        else:
            interest_amt = 1.05**float((month-month_pur-1))
            purchase_history[i][3] = float(purchase_history[i][0])*interest_amt
            cur_balance_owing_intst += float(purchase_history[i][0])*interest_amt


# Return True when it is the end of the month.

def is_end_of_month(day, month):
    ends_31 = [1,3,5,7,8,9,12]
    ends_29 = [2]
    if month in ends_31:
        if day == 31:
            return True
    elif month in ends_29:
        if day == 29:
            return True
    else:
        if day == 30:
            return True

    
# Simulate a purchase of amount amount, on date (day, month), in country country.
# Will stop the purchase if an error or fraud is detected. The purchase is added
# to purchase_history so its interest can be calculated at later dates.

def purchase(amount, day, month, country):
    global purchase_history, card_disabled, last_country, last_country2
    global cur_balance_owing_recent, last_update_day, last_update_month
    if card_disabled:
        return "error"
    else:
        fraud_detector(country)
        if card_disabled:
            return 'error'
    if error_detector(day, month):
        return "error"
    else:
        interest_calculator(month)
        purchase_history.append([amount, day, month, amount])
        last_country2 = last_country
        last_country = country
        last_update_day, last_update_month = day, month
    

# Return the current amount owed as of date (day, month).

def amount_owed(day, month):
    global purchase_history, cur_balance_owing_recent, card_disabled, last_update_day, last_update_month
    if error_detector(day, month):
        last_update_day, last_update_month = day, month
        return "error"
    interest_calculator(month)
    return float(cur_balance_owing_recent) + float(cur_balance_owing_intst)
    

# Simulate the credit card bill paying by paying amount, first 
# to cur_balance_owing_intst (which is the current balance of 
# unpaid fees which are acruing interest), and then to the 
# cur_balance_owing_recent (which is the current balance of the
# current months fees). This function also updates the purchases
# in purchase_history, deducting the amount with and without 
# interest for future simulations.

def pay_bill(amount, day, month):
    global cur_balance_owing_recent, cur_balance_owing_intst, purchase_history, last_update_day, last_update_month
    # if card_disabled:
    #     last_update_day, last_update_month = day, month
    #     return "error"
    if error_detector(day, month):
        return "error"
    temp_amt = amount
    last_update_day, last_update_month = day, month
    interest_calculator(month)
    for i in range(len(purchase_history)):
        if purchase_history[i][3] <= temp_amt:
            temp_amt -= purchase_history[i][3]
            purchase_history[i][3] = 0
            purchase_history[i][0] = 0
            interest_calculator(month)
        else:
            purchase_history[i][0] -= temp_amt/(purchase_history[i][3]/purchase_history[i][0])
            purchase_history[i][3] -= temp_amt
            interest_calculator(month)
            break

# Initialize all global variables outside the main block.
initialize()		
    
if __name__ == '__main__': 
    
    initialize()

    print(all_three_different(1,2,None))

    purchase(10,1,1,"Canada")
    purchase(10,2,1,"US")
    purchase(10,3,1,"France")
    purchase(10,1,12,"Canada")
    print(purchase_history)
    print(last_update_day, last_update_month)

    print("Now owing:", amount_owed(1,1), " (1,1)")
    print(purchase(100,3,1, "Canada"))
    print(purchase(101,3,2, "Canada"))
    print(purchase(120,2,1, "Canada"))
    print(purchase(140,3,3, "Canada"))
    print(last_update_day)
    print(last_update_month)
    print(purchase(101,3,4, "Germany"))
    print(purchase(100,3,5, "Sweden"))
    print(purchase(101,3,5, "Canada"))
    print(card_disabled)
    print("Now owing:", amount_owed(3,5), " (3,5)")
    print(purchase(1000,4,5,"gu"))
    print(purchase_history)
    print(error_detector(3,6))
    print(last_update_day)
    print(last_update_month)