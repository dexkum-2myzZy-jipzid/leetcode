class Solution {
    func sum(_ num1: Int, _ num2: Int) -> Int {
        return num1 + num2
    }
}

class Solution {
    func sum(_ num1: Int, _ num2: Int) -> Int {
        var a = num1, b = num2

        while b != 0 {
            let sumWithNoCarry = a ^ b
            let carry = (a & b) << 1

            a = sumWithNoCarry
            b = carry
        }

        return a
    }
}
