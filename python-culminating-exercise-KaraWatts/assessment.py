import re

# Main function
def exact_change(item_cost, money_paid):
    # initial test cases for value errors
    try:
        if item_cost > money_paid:
            return "You can't afford this item."
    except:
        return "Numeric values only - please try again"

    # value rounded to 2 to correct for random subraction errors
    total_change = round(money_paid - item_cost, 2)

    # Dictionary to store dollar bill denomations with their corresponding values as keys
    dollar_denominations = {
        100: "One Hundred Dollar Bill",
        50: "Fifty Dollar Bill",
        20: "Twenty Dollar Bill",
        10: "Ten Dollar Bill",
        5: "Five Dollar Bill",
        2: "Two Dollar Bill",
        1: "One Dollar Bill",
        0.25: "Quarter",
        0.10: "Dime",
        0.05: "Nickle",
        0.01: "Penny"
    }

    # list to store strings of number of coins/bills and the verbose denominations
    change_given = []
    change_owed = total_change
    # loop through denominations dictionary and calculate the number of bills or coins evenly divided into the amount owed and subtracting that value from the amount owed until it hits 0
    for cash_value in dollar_denominations:
        if cash_value <= change_owed:
            #divide the amount owed by the cash value and round down to whole number to give the number of bills/coins of that denomination that goes into the current amount balance - used int to ensure that no float values passed through
            cash_count = int(change_owed//cash_value)
            #subtract product of the cash value times the number of bills/coins that divide evenly into the amount owed and round down to 2 decimals to correct for weird subtraction errors
            change_owed = round((change_owed - cash_count*cash_value), 2)
            # construct string with number of bills/coins and the verbose denomination the associated coins
            text_output = f"{cash_count} {dollar_denominations[cash_value]}"
            # check for plurals if there are more than 1 bills/coins
            if cash_count >= 2:
                # account for penny to pennies if plural
                if dollar_denominations[cash_value] == 'Penny':
                    text_output = re.sub('y', 'ies', text_output)
                # adds s to end of every other plural
                else:
                    text_output += "s"
            # add completed string onto end of change_given list
            change_given.append(text_output)
    
    # join all but the last string in list together separated by commas
    change_str = ', '.join(change_given[:-1])


    # match cases to account for differences in setance structure depending on the amount of cash denominations needed to give change 
    match len(change_given):
        case 0:
            return (f'Your total is {total_change:.2f}.')
        case 1:
            return (f'Your total is {total_change:.2f}: {change_given[0]}.')
        case 2:
            return (f'Your total is {total_change:.2f}: {change_str} and {change_given[-1]}.')
        case _:
            return (f'Your total is {total_change:.2f}: {change_str}, and {change_given[-1]}.')
