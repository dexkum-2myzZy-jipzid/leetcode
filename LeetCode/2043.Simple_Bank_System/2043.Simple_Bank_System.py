#!/usr/bin/env python3


class Bank:

    def __init__(self, balance: List[int]):
        self.account = [inf] + balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            account1 < len(self.account)
            and account2 < len(self.account)
            and self.account[account1] >= money
        ):
            self.account[account1] -= money
            self.account[account2] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account < len(self.account):
            self.account[account] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if len(self.account) <= account or self.account[account] < money:
            return False
        else:
            self.account[account] -= money
            return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
