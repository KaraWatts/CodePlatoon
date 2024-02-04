def credit_check(cc_num):
    

# split string into array
    num_list = list(map(int,str(cc_num)))

# reverse array
    num_list.reverse()
    print(num_list)
# 2x every other digit
    double_every_other = [num*2 if index%2 == 0 else num for index, num in enumerate(num_list)]
    print(double_every_other)
# sum all digits
# sum % 10 == 0
credit_check(5541808923795240)


# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

