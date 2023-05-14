class BankAccount:
    def __init__(self, name, account_number, account_balance):
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance

    def add_money(self, summ):
        self.account_balance += summ

    def withdraw_money(self, summ):
        self.account_balance -= summ


bank_account = BankAccount('Victor', '505', 1000000)

print(bank_account.account_balance)
bank_account.add_money(1)
print(bank_account.account_balance)
bank_account.withdraw_money(100)
print(bank_account.account_balance)


