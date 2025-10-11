class Solution {
    func countPrimes(_ n: Int) -> Int {
        guard n > 1 else { return 0 }

        var isPrime = Array(repeating: true, count: n)
        isPrime[0] = false
        isPrime[1] = false

        var p = 2
        while p * p < n {
            if isPrime[p] {
                var m = p * p
                while m < n {
                    isPrime[m] = false
                    m += p
                }
            }
            p += 1
        }

        return isPrime.reduce(0) { $0 + ($1 ? 1 : 0) }
    }
}
