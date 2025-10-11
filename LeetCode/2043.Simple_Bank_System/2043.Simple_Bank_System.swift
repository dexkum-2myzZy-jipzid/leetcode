
class Bank {
    var balance: [Int]
    let n: Int

    init(_ balance: [Int]) {
        self.balance = [0] + balance
        n = balance.count
    }

    private func checkAccount(_ acc: Int, _ amount: Int) -> Bool {
        guard acc >= 1 && acc <= n && balance[acc] >= amount else { return false }
        return true
    }

    func transfer(_ account1: Int, _ account2: Int, _ money: Int) -> Bool {
        if checkAccount(account1, money) && checkAccount(account2, 0) {
            balance[account1] -= money
            balance[account2] += money
            return true
        } else {
            return false
        }
    }

    func deposit(_ account: Int, _ money: Int) -> Bool {
        if checkAccount(account, 0) {
            balance[account] += money
            return true
        } else {
            return false
        }
    }

    func withdraw(_ account: Int, _ money: Int) -> Bool {
        if !checkAccount(account, money) {
            return false
        } else {
            balance[account] -= money
            return true
        }
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj = Bank(balance)
 * let ret_1: Bool = obj.transfer(account1, account2, money)
 * let ret_2: Bool = obj.deposit(account, money)
 * let ret_3: Bool = obj.withdraw(account, money)
 */
