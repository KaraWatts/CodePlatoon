def credit_check(cc_num):
    

# split string into array
    num_list = list(map(int,str(cc_num)))

# reverse array
    num_list.reverse()

# 2x every other digit
    double_every_other = [num*2 if index%2 != 0 else num for index, num in enumerate(num_list)]
    
# sum digits of all products over 9
    summed_products = [(int(str(num)[0]) + int(str(num)[1])) if num>9 else num for num in double_every_other]


# sum all digits
    total_sum = 0
    for num in summed_products:
        total_sum += num
# sum % 10 == 0
    validation = "The number is valid!" if total_sum % 10 == 0 else "The number is invalid!"
    return validation





# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

