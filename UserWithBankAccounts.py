class User:
    def __init__(self, first_name, last_name, email, age, int_rate = 0.02, balance = 500):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount()

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email Address: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}\r")

    def enroll(self):
        if self.is_rewards_member == True:
            print("NOTICE User already a member")
        else: self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else: print("Insufficient Points")
        return self
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Member Name: {self.first_name} {self.last_name}")
        self.account.display_account_info()
        return self

class BankAccount:
    accounts = []
    def __init__(self, int_rate = 0.02, balance = 500.00):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount <= self.balance and amount >= 0:
            self.balance -= amount
        elif amount >= self.balance:
            print("Insufficient funds: Charing a $5 fee")
            self.balance -= 5.00
        return self

    def display_account_info(self):
        print(f"Account Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance += (self.balance * 2) * self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

Hermon = User("Hermon", "Rigsby", "hermon@msn.com", 25)
Hermon.spend_points(50).display_info()

Moby = User("Moby", "Dick", "mo-d@msn.com", 150)
Moby.enroll().spend_points(80).display_info()
Moby.enroll().display_info()

Chris = User("Chris", "Rock", "crock@msn.com", 51)
Chris.spend_points(40).display_info()
Chris.make_deposit(5.00).make_withdrawl(200).display_user_balance()