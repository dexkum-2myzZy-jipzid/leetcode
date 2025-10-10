class Solution {
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        // min k, eat all in h hours
        // 1, 2, 2, 2
        let n = piles.count

        func canEatAll(_ k: Int) -> Bool {
            var time = 0
            for p in piles {
                time += (p + k - 1) / k
            }
            return time <= h
        }

        var l = 1, r = piles.max()! + 1
        var res = Int.max

        while l < r {
            let m = (l + r) / 2
            if canEatAll(m) {
                r = m
            } else {
                l = m + 1
            }
        }

        return l
    }
}
