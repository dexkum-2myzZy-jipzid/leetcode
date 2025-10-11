class Solution {
    func shipWithinDays(_ weights: [Int], _ days: Int) -> Int {
        let n = weights.count
        var l = weights.max()!, r = weights.reduce(0, +) + 1

        // can ship within days
        func canShip(_ w: Int) -> Bool {
            var res = 1, prev = 0
            for cur in weights {
                if cur + prev > w {
                    res += 1
                    prev = cur
                } else {
                    prev += cur
                }
            }
            return res <= days
        }

        var res = Int.max
        while l < r {
            let m = (l + r) / 2
            if canShip(m) {
                r = m
                res = min(res, m)
            } else {
                l = m + 1
            }
        }

        return res
    }
}
