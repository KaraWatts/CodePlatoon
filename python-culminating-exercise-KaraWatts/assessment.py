import re


# function to split dollar and coin values
def dollars_split(total):
    return f'{total}'.split(".")


# Calculate the amount of bills needed per denomination and give a string output
def calculate_change(amount_owed, denominations):
    change_given = []

    for cash_value in denominations:
        if cash_value <= amount_owed:
            cash_count = amount_owed//cash_value
            amount_owed -= cash_count*cash_value
            text_output = f"{cash_count} {denominations[cash_value]}"

            if cash_count >= 2:
                if denominations[cash_value] == 'Penny':
                    text_output = re.sub('y', 'ies', text_output)
                else:
                    text_output += "s"

            change_given.append(text_output)

    return change_given


# Main function
def exact_change(item_cost, money_paid):
    # initial test cases for value errors
    try:
        if item_cost > money_paid:
            return "You can't afford this item."
    except:
        return "Numeric values only - please try again"

    # value rounded to 2 to correct for random subraction errors
    change_owed = round(money_paid - item_cost, 2)

    # test for value error if given whole dollar amounts
    try:
        dollars_owed, coins_owed = dollars_split(change_owed)
    except:
        dollars_owed, coins_owed = dollars_split(change_owed)+[0]

    # Dictionary to store dollar bill denomations with their corresponding values as keys
    dollar_denominations = {
        100: "One Hundred Dollar Bill",
        50: "Fifty Dollar Bill",
        20: "Twenty Dollar Bill",
        10: "Ten Dollar Bill",
        5: "Five Dollar Bill",
        2: "Two Dollar Bill",
        1: "One Dollar Bill"
    }
    # Dictionary to store coin denomations with their corresponding values as keys
    cent_denominations = {
        25: "Quarter",
        10: "Dime",
        5: "Nickle",
        1: "Penny"
    }

    # combine dollar and cent string lists
    change_list = calculate_change(
        int(dollars_owed), dollar_denominations) + calculate_change(int(coins_owed), cent_denominations)

    # join all but the last string in list together separated by commas
    change_str = ', '.join(change_list[:-1])

    # match cases to account for differences in setance structure depending on the amount of cash denominations needed to give change
    match len(change_list):
        case 0:
            return (f'Your total is {change_owed:.2f}.')
        case 1:
            return (f'Your total is {change_owed:.2f}: {change_list[0]}.')
        case 2:
            return (f'Your total is {change_owed:.2f}: {change_str} and {change_list[-1]}.')
        case _:
            return (f'Your total is {change_owed:.2f}: {change_str}, and {change_list[-1]}.')
