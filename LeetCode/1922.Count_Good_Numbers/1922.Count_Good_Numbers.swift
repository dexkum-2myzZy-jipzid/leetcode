class Solution {
    let MOD = 1_000_000_007

    func countGoodNumbers(_ n: Int) -> Int {
        let evenCount = (n + 1) / 2
        let oddCount = n / 2

        let even = powMod(5, evenCount)
        let odd = powMod(4, oddCount)

        return even * odd % MOD
    }

    // exp >= 0
    func powMod(_ num: Int, _ exp: Int) -> Int {
        var b = num, e = exp
        var res = 1

        while e > 0 {
            if e & 1 == 1 {
                res = (res * b) % MOD
            }
            b = (b * b) % MOD
            e >>= 1
        }
        return res
    }
}
