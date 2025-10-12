class Solution {
    func decimalRepresentation(_ n: Int) -> [Int] {
        var m = n, x = 1
        var res: [Int] = []

        while m > 0 {
            let d = m % 10
            if d > 0 {
                res.append(x * d)
            }
            x *= 10
            m /= 10
        }

        res.sort(by: >)

        return res
    }
}
