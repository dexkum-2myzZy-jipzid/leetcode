class Solution {
    func maxProfit(_ prices: [Int], _ strategy: [Int], _ k: Int) -> Int {
        // -1, buy one unit, 0 hold, 1 sell
        // k is even
        // 4 * 0 + 2 * 1 = 2
        // max profit
        let n = prices.count
        var prefixSum = [0]
        var prefixPrice = [0]

        for (p, s) in zip(prices, strategy) {
            if let last = prefixSum.last {
                prefixSum.append(last + p * s)
            }
            if let last = prefixPrice.last {
                prefixPrice.append(last + p)
            }
        }

        var l = 0, r = k
        var res = prefixSum[n]
        while r <= n {
            let original = prefixSum[n] - (prefixSum[r] - prefixSum[l])
            let modify = prefixPrice[r] - prefixPrice[r - k / 2]
            res = max(res, original + modify)
            l += 1
            r += 1
        }

        return res
    }
}
