class Solution {
    func myPow(_ x: Double, _ n: Int) -> Double {
        if n == 0 { return 1.0 }
        if x == 0 { return 0.0 }

        var e: Int = n, base: Double = x
        if e < 0 {
            e = -e
            base = 1.0 / base
        }

        var res = 1.0
        while e > 0 {
            if e & 1 == 1 {
                res *= base
            }

            base *= base
            e >>= 1
        }

        return res
    }
}
