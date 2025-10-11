class Solution {
    func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
        let max = candies.max()!
        var res = Array(repeating: false, count: candies.count)

        for (i, c) in candies.enumerated() {
            if c + extraCandies >= max {
                res[i] = true
            }
        }

        return res
    }
}
