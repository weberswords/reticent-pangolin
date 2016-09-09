#Created Feb 2016

import math

principal = input("How much would you like to borrow? ")
principal = float(principal)
term = input("How many months would you like to borrow? ")
term = float(term)
interest = 0.09

def interest_calc():
    if principal >= 2000 or term >= 12:
        interest = 0.045
    if principal < 2000 or term < 12:
        interest = 0.08
    return interest

interest_calc()

value = (1+interest/12)
value = float(value)
end_total = math.pow(value, term)
final = principal * end_total
print("You will pay back %d." % final)


payment = input("Payment amount: ")
payment = float(payment)
final -= payment
print("Your new balance is %d" % final)


