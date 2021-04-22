# register
# - first_name, last_name, password, email
# - create user account


# login
# - account_no and password

# bank activities
# starting up the banking systems
import random

# dictionary
database = {}


def init():
    isValidOptionSelected = False
    print("Welcome to InternationalBank")

    while not isValidOptionSelected:

        get_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

        if get_account == 1:
            isValidOptionSelected = True
            login()
        elif get_account == 2:
            isValidOptionSelected = True
            print(register())

        else:
            print("You have selected an invalid option")


def login():
    print("****Login to your account***")

    acctNumberFromUser = int(input("what is your account number? \n"))
    password = input("What is your password \n")

    for account_no, userdetails in database.items():
        if account_no == acctNumberFromUser:
            if userdetails[3] == password:
                bank_activities(userdetails)

    print('Invalid account or password')


def register():
    print("*** Registration ***")
    email = (input("what is your email address? \n"))
    first_name = input("what is your first name \n")
    last_name = input("what is your last name \n")
    password = input("generate a self password \n")

    account_no = getAccountNo()
    database[account_no] = [first_name, last_name, email, password]

    print("Your account has been created")
    print(" == === ===== ==== ===")
    print("Your account number is: %d" % account_no)
    print("Make sure you keep it safe")
    print("== === ===== ==== ===")

    login()


def bank_activities(user):
    print("Welcome %s %s " % (user[0], user[1]))

    transaction = int(input("What would you like to do? (1) check balance (2) withdrawal (3) cash_deposit (4) logout "
                            "(5) exit \n"))

    if transaction == 1:
        checkbalance()

    elif transaction == 2:
        withdrawcash()

    elif transaction == 3:
        depositcash()

    elif transaction == 4:
        logout()

    elif transaction == 5:
        exit()
    else:
        print("Invalid option")
        bank_activities(user)


def check_balance():
    account_balance = float(10000.55)
    print("\n Net Available Balance =", account_balance)


def withdraw_cash():
    account_balance = float(10000.55)
    user_withdrawal = float(input("Enter amount to be withdrawn: "))
    if user_withdrawal > account_balance:
        balance = account_balance - user_withdrawal
        print("\n You withdrew:", user_withdrawal, "\n your new current balance is:", balance)
    else:
        print('\n Insufficient balance')


def deposit_cash():
    account_balance = float(10000.55)
    user_deposit = float(input("Enter amount to be Deposited: "))
    balance = account_balance + user_deposit
    print("\n Amount deposited:", balance)


def getAccountNo():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


# ACTUAL BANKING SYSTEM #


init()
