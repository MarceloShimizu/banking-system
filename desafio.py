options = """

----------- TRANSACTIONS -----------

1 - Deposit
2 - Withdraw
3 - Statement
0 - Exit

------------------------------------

"""

balance = 0
amount = 0
withdrawal_limit = 500
statement = ""
withdrawal_quantity = 0
MAXIMUM_WITHDRAWALS = 3

while True:

    print(options)
    chosen_option = input("Type the transaction desired: ")

    if chosen_option == "1":

        amount = float(input("Type the amount of the deposit: "))

        if amount > 0:
            balance += amount
            statement += f"Deposit: $ {amount:.2f}\n"

        else:
            print("\nTransaction Failed! The amount typed in is invalid.")

    elif chosen_option == "2":
        amount = float(input("Type the amount of the withdrawal:"))

        exceeded_balance = amount > balance

        exceeded_withdrawal_limit = amount > withdrawal_limit

        exceeded_withdrawal_quantity = withdrawal_quantity >= MAXIMUM_WITHDRAWALS

        if exceeded_balance:
            print("\nTransaction Failed! There are insufficient funds in this account.")

        elif exceeded_withdrawal_limit:
            print("\nTransaction Failed! The amount exceeds the daily withdrawal limit.")

        elif exceeded_withdrawal_quantity:
            print("\nTransaction Failed! Maximum number of withdrawals exceeded.")

        elif amount > 0:
            balance -= amount
            statement += f"Withdrawal: $ {amount:.2f}\n"
            withdrawal_quantity += 1

        else:
            print("\nTransaction Failed! The amount typed in is invalid.")

    elif chosen_option == "3":
        print("\n================ STATEMENT ================")
        print("No transactions were completed." if not statement else statement)
        print(f"\nBalance: $ {balance:.2f}")
        print("===========================================")

    elif chosen_option == "0":
        break

    else:
        print("\nInvalid Transaction, please select the correct option.")
