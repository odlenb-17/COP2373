# Bank Account Class Assignment

class BankAcct:

    # Constructor

    def __init__(self, name, account_number, amount, interest_rate):

        self.name = name

        self.account_number = account_number

        self.amount = amount

        self.interest_rate = interest_rate

    # Deposit money

    def deposit(self, money):

        self.amount += money

    # Withdraw money

    def withdraw(self, money):

        if money <= self.amount:

            self.amount -= money

        else:

            print("Insufficient funds.")

    # Change interest rate

    def adjust_interest_rate(self, new_rate):

        self.interest_rate = new_rate

    # Return balance

    def get_balance(self):

        return self.amount

    # Calculate interest

    def calculate_interest(self, days):

        interest = self.amount * (self.interest_rate / 100) * (days / 365)

        return interest

    # String method

    def __str__(self):

        return (f"Account Holder: {self.name}\n"

                f"Account Number: {self.account_number}\n"

                f"Balance: ${self.amount:.2f}\n"

                f"Interest Rate: {self.interest_rate}%")

# Test Function

def test_bank_account():

    account = BankAcct("John Smith", "123456789", 1000.00, 4.5)

    print("Original Account")

    print(account)

    print()

    account.deposit(500)

    print("After Depositing $500")

    print(f"Balance: ${account.get_balance():.2f}")

    print()

    account.withdraw(200)

    print("After Withdrawing $200")

    print(f"Balance: ${account.get_balance():.2f}")

    print()

    account.adjust_interest_rate(5.0)

    print("New Interest Rate: 5.0%")

    print()

    interest = account.calculate_interest(90)

    print(f"Interest for 90 days: ${interest:.2f}")

    print()

    print("Final Account Information")

    print(account)

# Run the test

test_bank_account()