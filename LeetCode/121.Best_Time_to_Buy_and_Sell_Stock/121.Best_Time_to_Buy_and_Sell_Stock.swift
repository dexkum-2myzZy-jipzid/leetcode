class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        let n = prices.count
        var min_p = prices[0]
        var res = 0

        for i in 1 ..< n {
            res = max(prices[i] - min_p, res)
            min_p = min(min_p, prices[i])
        }

        return res
    }
}
