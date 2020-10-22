balance = 0
user_input = 0
while user_input != 4:
    print('1.) Deposit')
    print('2.) Withdraw')
    print('3.) Check Balance')
    print('4.) Exit')
    user_input = int(input('Pick an option: '))
    if user_input == 1:
        deposit = int(input('How much to deposit? '))
        balance += deposit
    elif user_input == 2:
        withdraw = int(input('How much to withdraw? '))
        if withdraw > balance:
            print('Insufficient funds')
        else:
            balance -= withdraw
    elif user_input == 3:
        print('Your balance is:', balance)