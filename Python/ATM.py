'''Created January 2016
    ask if you want to check balance, withdraw, deposit
    check balance; give balance
    withdraw
    ask how much
    notify of fee
    subtract from balance
    deposit
    ask how much
    add to balance
'''

def ATM():
    balance_total = 2000
    while True:
        command = input('Would you like to get your balance, withdraw, or deposit? Type B for balance, '
                'W for withdraw, or D for deposit: ')
        if command.upper() == 'B':
            print('Your balance is %d.' % balance_total)
        elif command.upper() == 'W':
            fee = input('There is a $3 fee for using this machine. Would you like to accept? Y or N: ')
            if fee.upper() == "N":
                ATM()
            elif fee.upper() == "Y":
                pass
            else:
                print("That input is not recognized.")
                ATM()
            w_amount = input('How much would you like to withdraw? ')
            w_amount = float(w_amount)
            if w_amount > balance_total:
                print("You're too poor for that. Your current balance is %d." % balance_total)
            elif float(w_amount) <= float(balance_total):
                new_balance = float(balance_total) - (float(w_amount) + 3)
                balance_total = float(new_balance)
                print('After withdrawing, your balance is now %d.' % balance_total)
            else:
                print ('That is not a number. Please try again.')
        elif command.upper() == 'D':
            d_amount = input('How much would you like to deposit? ')
            fee = input('There is a $3 fee for using this machine. Would you like to accept? Y or N: ')
            if fee.upper() == "N":
                ATM()
            elif fee.upper() == "Y":
                pass
            else:
                print("That input is not recognized.")
                ATM()
            new_balance = float(balance_total) + (float(d_amount) - 3)
            balance_total = float(new_balance)
            print('After depositing, your balance is now %d.' % balance_total)
        else:
            print('That command is not recognized.')

ATM()